from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass, field

import requests

logger = logging.getLogger(__name__)


#  Data model 

@dataclass
class Peer:
    
    node_id: str
    host: str
    port: int
    last_seen: float = field(default_factory=time.time)

    @property
    def address(self) -> str:
        return f"http://{self.host}:{self.port}"

    def update_heartbeat(self) -> None:
        self.last_seen = time.time()

    def is_alive(self, timeout_seconds: int = 30) -> bool:
        return (time.time() - self.last_seen) < timeout_seconds

    def to_dict(self) -> dict:
        return {
            "node_id": self.node_id,
            "host": self.host,
            "port": self.port,
            "address": self.address,
            "last_seen": self.last_seen,
        }
    
#   Bootstrap node setup    

class PeerRegistry:

    EVICTION_INTERVAL_SECONDS = 15   
    PEER_TIMEOUT_SECONDS      = 30   

    def __init__(self):
        self._peers: dict[str, Peer] = {}   
        self._lock = threading.Lock()

        self._eviction_thread = threading.Thread(
            target=self._eviction_loop,
            daemon=True,
            name="peer-eviction",
        )
        self._eviction_thread.start()
        logger.info("[PeerRegistry] Started with eviction interval=%ds", self.EVICTION_INTERVAL_SECONDS)

    def register(self, node_id: str, host: str, port: int) -> None:
        
        with self._lock:
            if node_id in self._peers:
                self._peers[node_id].update_heartbeat()
                logger.debug("[PeerRegistry] Heartbeat from %s", node_id)
            else:
                self._peers[node_id] = Peer(node_id=node_id, host=host, port=port)
                logger.info("[PeerRegistry] New peer registered: %s @ %s:%d", node_id, host, port)

    def get_live_peers(self, exclude_id: str | None = None) -> list[Peer]:
        
        with self._lock:
            return [
                p for p in self._peers.values()
                if p.is_alive(self.PEER_TIMEOUT_SECONDS)
                and p.node_id != exclude_id
            ]

    def peer_count(self) -> int:
        with self._lock:
            return sum(1 for p in self._peers.values() if p.is_alive(self.PEER_TIMEOUT_SECONDS))

    def _eviction_loop(self) -> None:
        
        while True:
            time.sleep(self.EVICTION_INTERVAL_SECONDS)
            with self._lock:
                dead = [
                    node_id for node_id, peer in self._peers.items()
                    if not peer.is_alive(self.PEER_TIMEOUT_SECONDS)
                ]
                for node_id in dead:
                    del self._peers[node_id]
                    logger.info("[PeerRegistry] Evicted unresponsive peer: %s", node_id)    
from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass, field

import requests

logger = logging.getLogger(__name__)


# ── Data model ────────────────────────────────────────────────────────────────

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
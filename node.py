import argparse
import logging
import sys
import threading

from flask import Flask, jsonify, render_template, request

from core.search_engine import SearchEngine
from data.papers import PAPERS
from network.discovery import DiscoveryClient, PeerRegistry

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("nexus.node")

app = Flask(__name__)

_engine: SearchEngine | None = None
_node_id: str | None = None
_registry: PeerRegistry | None = None      
_discovery: DiscoveryClient | None = None  

#   Search routes 

@app.get("/")
def home():
    return render_template(
        "index.html",
        node_id=_node_id,
        paper_count=_engine.paper_count,
    )


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "node_id": _node_id,
        "papers_indexed": _engine.paper_count,
        "embedding_dim": _engine.embedding_dim,
        "is_bootstrap": _registry is not None,
        "known_peers": _registry.peer_count() if _registry else None,
    })


@app.get("/search")
def search():
    query = request.args.get("q", "").strip()
    top_k = request.args.get("k", 5, type=int)

    if not query:
        return jsonify({"error": "Missing required query parameter 'q'."}), 400

    if top_k < 1 or top_k > 50:
        return jsonify({"error": "Parameter 'k' must be between 1 and 50."}), 400

    try:
        results = _engine.search(query, top_k=top_k)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "node_id": _node_id,
        "query": query,
        "results": [
            {
                "paper_id": r.paper_id,
                "title": r.title,
                "abstract": r.abstract,
                "year": r.year,
                "domain": r.domain,
                "score": round(r.score, 4),
                "node_id": r.node_id,
            }
            for r in results
        ],
    })

#   Peer discovery routes 

@app.post("/peers/register")
def peers_register():
   
    if _registry is None:
        return jsonify({
            "error": "This node is not a bootstrap node."
        }), 403

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Expected JSON body."}), 400

    node_id = data.get("node_id")
    host    = data.get("host")
    port    = data.get("port")

    if not all([node_id, host, port]):
        return jsonify({
            "error": "Required fields: node_id, host, port."
        }), 400

    _registry.register(node_id=node_id, host=host, port=int(port))

    return jsonify({
        "status": "registered",
        "node_id": node_id,
    })


@app.get("/peers/list")
def peers_list():
    
    if _registry is None:
        return jsonify({
            "error": "This node is not a bootstrap node."
        }), 403

    exclude_id = request.args.get("exclude")
    live_peers = _registry.get_live_peers(exclude_id=exclude_id)

    return jsonify({
        "peers": [p.to_dict() for p in live_peers],
        "count": len(live_peers),
    })

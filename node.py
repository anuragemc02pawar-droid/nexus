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
_discovery: DiscoveryClient | None = None  ++
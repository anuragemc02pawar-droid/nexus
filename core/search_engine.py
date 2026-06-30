from __future__ import annotations

import logging
import time
from dataclasses import dataclass

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)
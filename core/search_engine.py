from __future__ import annotations

import logging
import time
from dataclasses import dataclass

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

@dataclass
class SearchResult:
    paper_id: str
    title: str
    abstract: str
    year: int
    domain: str
    score: float
    node_id: str


class SearchEngine:

    EMBED_TEMPLATE = "{title}. {abstract}"

    def __init__(
        self,
        papers: list[dict],
        node_id: str,
        model_name: str = "all-MiniLM-L6-v2",
    ):
        if not papers:
            raise ValueError("Cannot build a SearchEngine with an empty corpus.")

        self.papers = papers
        self.node_id = node_id

        logger.info("[%s] Loading embedding model '%s'", node_id, model_name)
        self._model = SentenceTransformer(model_name)

        self._index: faiss.IndexFlatIP | None = None
        self._build_index()

    def _paper_to_text(self, paper: dict) -> str:
        return self.EMBED_TEMPLATE.format(
            title=paper["title"],
            abstract=paper["abstract"],
        )

    def _build_index(self) -> None:
        logger.info("[%s] Encoding %d papers...", self.node_id, len(self.papers))
        t0 = time.perf_counter()

        texts = [self._paper_to_text(p) for p in self.papers]

        embeddings = self._model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        embeddings = np.array(embeddings, dtype=np.float32)

        dim = embeddings.shape[1]
        self._index = faiss.IndexFlatIP(dim)
        self._index.add(embeddings)

        elapsed = time.perf_counter() - t0
        logger.info(
            "[%s] Index ready — %d vectors, dim=%d, built in %.2fs",
            self.node_id, self._index.ntotal, dim, elapsed,
        )

    def search(self, query: str, top_k: int = 5) -> list[SearchResult]:
        if not query.strip():
            raise ValueError("Search query cannot be empty.")

        top_k = min(top_k, len(self.papers))

        query_vec = self._model.encode(
            [query],
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        query_vec = np.array(query_vec, dtype=np.float32)

        scores, indices = self._index.search(query_vec, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < 0:
                continue

            paper = self.papers[idx]
            results.append(SearchResult(
                paper_id=paper["id"],
                title=paper["title"],
                abstract=paper["abstract"],
                year=paper.get("year", 0),
                domain=paper.get("domain", "unknown"),
                score=float(score),
                node_id=self.node_id,
            ))

        return results

    @property
    def paper_count(self) -> int:
        return len(self.papers)

    @property
    def embedding_dim(self) -> int:
        return self._index.d if self._index else 0

    def __repr__(self) -> str:
        return (
            f"SearchEngine(node_id={self.node_id!r}, "
            f"papers={self.paper_count}, "
            f"dim={self.embedding_dim})"
        )
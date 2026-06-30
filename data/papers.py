PAPERS = [
    {
        "id": "vaswani2017",
        "title": "Attention Is All You Need",
        "abstract": (
            "We propose the Transformer, a model architecture eschewing recurrence "
            "and instead relying entirely on an attention mechanism to draw global "
            "dependencies between input and output."
        ),
        "year": 2017,
        "domain": "deep_learning",
    },
    {
        "id": "devlin2018",
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "abstract": (
            "We introduce BERT, which stands for Bidirectional Encoder Representations "
            "from Transformers. BERT is designed to pretrain deep bidirectional "
            "representations by jointly conditioning on both left and right context."
        ),
        "year": 2018,
        "domain": "deep_learning",
    },
    {
        "id": "shaw2018",
        "title": "Self-Attention with Relative Position Representations",
        "abstract": (
            "We extend the self-attention mechanism to efficiently consider "
            "representations of the relative positions between sequence elements, "
            "improving performance on machine translation tasks."
        ),
        "year": 2018,
        "domain": "deep_learning",
    },
    {
        "id": "reimers2019",
        "title": "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
        "abstract": (
            "We present Sentence-BERT, a modification of BERT that uses siamese "
            "and triplet network structures to derive semantically meaningful "
            "sentence embeddings that can be compared using cosine similarity."
        ),
        "year": 2019,
        "domain": "information_retrieval",
    },
    {
        "id": "johnson2019",
        "title": "Billion-scale similarity search with GPUs",
        "abstract": (
            "We describe a system for efficient similarity search and clustering of "
            "dense vectors, scaling to billions of vectors. This is the paper "
            "describing the FAISS library."
        ),
        "year": 2019,
        "domain": "information_retrieval",
    },
    {
        "id": "dense_retrieval2020",
        "title": "Dense Passage Retrieval for Open-Domain Question Answering",
        "abstract": (
            "We show that retrieval can be practically implemented using dense "
            "representations alone, where embeddings are learned from a small "
            "number of questions and passages."
        ),
        "year": 2020,
        "domain": "information_retrieval",
    },
    {
        "id": "jegou2011",
        "title": "Product Quantization for Nearest Neighbor Search",
        "abstract": (
            "We introduce a method for searching nearest neighbors in high-dimensional "
            "spaces using product quantization, achieving fast approximate search "
            "with low memory requirements."
        ),
        "year": 2011,
        "domain": "information_retrieval",
    },
    {
        "id": "lamport1982",
        "title": "The Byzantine Generals Problem",
        "abstract": (
            "We define the Byzantine Generals Problem: reliable distributed systems "
            "must handle components that give conflicting information to different "
            "parts of the system. We prove conditions under which this is solvable."
        ),
        "year": 1982,
        "domain": "distributed_systems",
    },
    {
        "id": "castro1999",
        "title": "Practical Byzantine Fault Tolerance",
        "abstract": (
            "We present a new algorithm for Byzantine-fault-tolerant state machine "
            "replication that is able to work correctly in asynchronous environments "
            "such as the Internet."
        ),
        "year": 1999,
        "domain": "distributed_systems",
    },
    {
        "id": "ongaro2014",
        "title": "In Search of an Understandable Consensus Algorithm (Raft)",
        "abstract": (
            "Raft is a consensus algorithm designed to be more understandable than "
            "Paxos. It separates the key elements of consensus — leader election, "
            "log replication, and safety — and enforces stronger coherency."
        ),
        "year": 2014,
        "domain": "distributed_systems",
    },
    {
        "id": "lamport2001",
        "title": "Paxos Made Simple",
        "abstract": (
            "The Paxos algorithm for implementing a fault-tolerant distributed "
            "service is presented in a simple, straightforward way. The algorithm "
            "follows almost unavoidably from the properties it is required to satisfy."
        ),
        "year": 2001,
        "domain": "distributed_systems",
    },
    {
        "id": "bft_fedavg2020",
        "title": "On the Byzantine-Robustness of Federated Averaging",
        "abstract": (
            "We analyze the robustness of federated averaging when a fraction of "
            "clients are Byzantine adversaries, and propose defenses based on "
            "robust aggregation rules."
        ),
        "year": 2020,
        "domain": "distributed_systems",
    },
    {
        "id": "maymounkov2002",
        "title": "Kademlia: A Peer-to-peer Information System Based on the XOR Metric",
        "abstract": (
            "We describe a peer-to-peer distributed hash table characterized by a "
            "novel XOR-based metric topology. This topology has provable consistency "
            "and performance in a fault-prone environment."
        ),
        "year": 2002,
        "domain": "p2p_networking",
    },
    {
        "id": "stoica2001",
        "title": "Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications",
        "abstract": (
            "Chord provides support for a single operation: given a key, it maps the "
            "key onto a node. It uses consistent hashing to assign keys to nodes, "
            "and adapts as nodes join and leave the system."
        ),
        "year": 2001,
        "domain": "p2p_networking",
    },
    {
        "id": "benet2014",
        "title": "IPFS: Content Addressed, Versioned, P2P File System",
        "abstract": (
            "We present the InterPlanetary File System, a peer-to-peer distributed "
            "file system that seeks to connect all computing devices with the same "
            "system of files using content-addressed storage."
        ),
        "year": 2014,
        "domain": "p2p_networking",
    },
    {
        "id": "nakamoto2008",
        "title": "Bitcoin: A Peer-to-Peer Electronic Cash System",
        "abstract": (
            "A purely peer-to-peer version of electronic cash allowing online payments "
            "without going through a financial institution, using a chain of digital "
            "signatures and a proof-of-work consensus mechanism."
        ),
        "year": 2008,
        "domain": "p2p_networking",
    },
    {
        "id": "gossip2007",
        "title": "Gossip Protocols for Large-Scale Distributed Systems",
        "abstract": (
            "Gossip-based protocols offer a robust and scalable way to disseminate "
            "information in large distributed networks. We survey epidemic algorithms "
            "and analyze their convergence and resilience properties."
        ),
        "year": 2007,
        "domain": "p2p_networking",
    },
    {
        "id": "kingma2014",
        "title": "Adam: A Method for Stochastic Optimization",
        "abstract": (
            "We introduce Adam, an algorithm for first-order gradient-based "
            "optimization based on adaptive estimates of lower-order moments. "
            "It is computationally efficient and well suited to large-scale problems."
        ),
        "year": 2014,
        "domain": "optimization",
    },
    {
        "id": "bottou2012",
        "title": "Stochastic Gradient Descent Tricks",
        "abstract": (
            "We present a collection of recommendations to train neural networks "
            "with stochastic gradient descent, covering learning rate schedules, "
            "momentum, and tricks to avoid local minima."
        ),
        "year": 2012,
        "domain": "optimization",
    },
    {
        "id": "ioffe2015",
        "title": "Batch Normalization: Accelerating Deep Network Training",
        "abstract": (
            "We propose batch normalization, a technique that normalizes layer inputs, "
            "allowing much higher learning rates, reducing dependence on careful "
            "initialization, and acting as a regularizer."
        ),
        "year": 2015,
        "domain": "deep_learning",
    },
    {
        "id": "mnih2013",
        "title": "Playing Atari with Deep Reinforcement Learning",
        "abstract": (
            "We present the first deep learning model to successfully learn control "
            "policies from high-dimensional sensory input using reinforcement learning, "
            "training on raw pixels from Atari games."
        ),
        "year": 2013,
        "domain": "reinforcement_learning",
    },
    {
        "id": "schulman2017",
        "title": "Proximal Policy Optimization Algorithms",
        "abstract": (
            "We propose PPO, a family of policy gradient methods that alternate "
            "between sampling data and optimizing a clipped surrogate objective, "
            "achieving strong performance with simpler implementation than TRPO."
        ),
        "year": 2017,
        "domain": "reinforcement_learning",
    },
    {
        "id": "goodfellow2014",
        "title": "Generative Adversarial Networks",
        "abstract": (
            "We propose a framework for estimating generative models via an "
            "adversarial process in which two networks — a generator and a "
            "discriminator — are trained simultaneously in a minimax game."
        ),
        "year": 2014,
        "domain": "deep_learning",
    },
    {
        "id": "he2015",
        "title": "Deep Residual Learning for Image Recognition",
        "abstract": (
            "We present a residual learning framework to ease the training of "
            "very deep networks. Residual networks are easier to optimize and "
            "can gain accuracy from considerably increased depth."
        ),
        "year": 2015,
        "domain": "deep_learning",
    },
    {
        "id": "srivastava2014",
        "title": "Dropout: A Simple Way to Prevent Neural Networks from Overfitting",
        "abstract": (
            "We describe dropout, a technique for preventing overfitting by "
            "randomly dropping units during training, which can be interpreted "
            "as sampling from an ensemble of different network architectures."
        ),
        "year": 2014,
        "domain": "deep_learning",
    },
    {
        "id": "mikolov2013",
        "title": "Efficient Estimation of Word Representations in Vector Space",
        "abstract": (
            "We propose two architectures — CBOW and Skip-gram — for computing "
            "continuous vector representations of words from large datasets. "
            "These representations capture semantic and syntactic relationships."
        ),
        "year": 2013,
        "domain": "deep_learning",
    },
    {
        "id": "dwork2006",
        "title": "Differential Privacy",
        "abstract": (
            "We introduce differential privacy, a rigorous mathematical definition "
            "of privacy for statistical databases and algorithms, providing a "
            "guarantee that no individual's data has significant influence on output."
        ),
        "year": 2006,
        "domain": "security",
    },
    {
        "id": "boneh2001",
        "title": "Public-Key Cryptography and Digital Signatures",
        "abstract": (
            "We survey the foundations of public-key cryptography and digital "
            "signature schemes, which provide authenticity, integrity, and "
            "non-repudiation in distributed systems."
        ),
        "year": 2001,
        "domain": "security",
    },
    {
        "id": "konecny2016",
        "title": "Federated Learning: Strategies for Improving Communication Efficiency",
        "abstract": (
            "We present federated learning, where multiple parties collaboratively "
            "train a model without sharing local data, with a focus on reducing "
            "communication costs between clients and a central server."
        ),
        "year": 2016,
        "domain": "distributed_systems",
    },
]


def get_slice(start: int, end: int) -> list[dict]:
    return PAPERS[start:end]


def get_by_domain(domain: str) -> list[dict]:
    return [p for p in PAPERS if p["domain"] == domain]
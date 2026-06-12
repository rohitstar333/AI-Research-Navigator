QUESTIONS = [

    # ==================================================
    # CONCEPT EXPLANATION (10)
    # ==================================================

    {
        "question": "What is attention?",
        "route": "concept_explanation",
        "expected_docs": [
            "Attention Is All You Need"
        ],
        "expected_section":
            "Scaled Dot-Product Attention",
    },

    {
        "question": "What is self-attention?",
        "route": "concept_explanation",
        "expected_docs": [
            "Attention Is All You Need"
        ],
    },

    {
        "question": "What is retrieval augmented generation?",
        "route": "concept_explanation",
        "expected_docs": [
            "Retrieval-Augmented Generation for Knowledge-Intensive NLP"
        ],
    },

    {
        "question": "What is chain-of-thought prompting?",
        "route": "concept_explanation",
        "expected_docs": [
            "Chain-of-Thought Prompting Elicits Reasoning in LLMs"
        ],
    },

    {
        "question": "What is RLHF?",
        "route": "concept_explanation",
        "expected_docs": [
            "Training Language Models to Follow Instructions"
        ],
    },

    {
        "question": "What is ReAct?",
        "route": "concept_explanation",
        "expected_docs": [
            "ReAct: Synergizing Reasoning and Acting in Language Models"
        ],
    },

    {
        "question": "What is LoRA?",
        "route": "concept_explanation",
        "expected_docs": [
            "LoRA: Low-Rank Adaptation of Large Language Models"
        ],
    },

    {
        "question": "What is FlashAttention?",
        "route": "concept_explanation",
        "expected_docs": [
            "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"
        ],
        "expected_section":
            "Introduction",
    },

    {
        "question": "What is mixture of experts?",
        "route": "concept_explanation",
        "expected_docs": [
            "Mixtral of Experts"
        ],
    },

    {
        "question": "What is GraphRAG?",
        "route": "concept_explanation",
        "expected_docs": [
            "From Local to Global: A Graph RAG Approach"
        ],
    },

    # ==================================================
    # PAPER DEEP DIVE (6)
    # ==================================================

    {
        "question": "Explain Attention Is All You Need",
        "route": "paper_deep_dive",
        "expected_docs": [
            "Attention Is All You Need"
        ],
    },

    {
        "question": "Explain BERT",
        "route": "paper_deep_dive",
        "expected_docs": [
            "BERT: Pre-training of Deep Bidirectional Transformers"
        ],
    },

    {
        "question": "Explain GPT-3",
        "route": "paper_deep_dive",
        "expected_docs": [
            "Language Models are Few-Shot Learners"
        ],
    },

    {
        "question": "Explain Llama 2",
        "route": "paper_deep_dive",
        "expected_docs": [
            "Llama 2: Open Foundation and Fine-Tuned Chat Models"
        ],
    },

    {
        "question": "Explain DeepSeek-V3",
        "route": "paper_deep_dive",
        "expected_docs": [
            "DeepSeek-V3 Technical Report"
        ],
    },

    {
        "question": "Explain Qwen2",
        "route": "paper_deep_dive",
        "expected_docs": [
            "Qwen2 Technical Report"
        ],
    },

    # ==================================================
    # COMPARE APPROACHES (6)
    # ==================================================

    {
        "question": "FlashAttention vs Standard Attention",
        "route": "compare_approaches",
        "expected_docs": [
            "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"
        ],
    },

    {
        "question": "CRAG vs GraphRAG",
        "route": "compare_approaches",
        "expected_docs": [
            "Corrective RAG (CRAG)",
            "From Local to Global: A Graph RAG Approach",
        ],
    },

    {
        "question": "LoRA vs Full Fine-Tuning",
        "route": "compare_approaches",
        "expected_docs": [
            "LoRA: Low-Rank Adaptation of Large Language Models"
        ],
    },

    {
        "question": "KTO vs SimPO",
        "route": "compare_approaches",
        "expected_docs": [
            "KTO: Model Alignment as Prospect Theoretic Optimization",
            "SimPO: Simple Preference Optimization",
        ],
    },

    {
        "question": "DeepSeek-R1 vs Chain-of-Thought Prompting",
        "route": "compare_approaches",
        "expected_docs": [
            "DeepSeek-R1: Incentivizing Reasoning Capability via RL",
            "Chain-of-Thought Prompting Elicits Reasoning in LLMs",
        ],
    },

    {
        "question": "Llama 3 vs Qwen2",
        "route": "compare_approaches",
        "expected_docs": [
            "The Llama 3 Herd of Models",
            "Qwen2 Technical Report",
        ],
    },

    # ==================================================
    # RECENT DEVELOPMENTS (6)
    # ==================================================

    {
        "question": "Recent developments in MoE",
        "route": "recent_developments",
        "expected_docs": [
            "Mixtral of Experts",
            "DeepSeek-V3 Technical Report",
        ],
    },

    {
        "question": "Recent developments in reasoning models",
        "route": "recent_developments",
        "expected_docs": [
            "DeepSeek-R1: Incentivizing Reasoning Capability via RL",
        ],
    },

    {
        "question": "Recent advances in preference optimization",
        "route": "recent_developments",
        "expected_docs": [
            "KTO: Model Alignment as Prospect Theoretic Optimization",
            "SimPO: Simple Preference Optimization",
        ],
    },

    {
        "question": "Recent advances in RAG",
        "route": "recent_developments",
        "expected_docs": [
            "Corrective RAG (CRAG)",
            "From Local to Global: A Graph RAG Approach",
            "RAFT: Adapting Language Model to Domain-Specific RAG",
        ],
    },

    {
        "question": "Latest open-weight LLMs",
        "route": "recent_developments",
        "expected_docs": [
            "The Llama 3 Herd of Models",
            "Qwen2 Technical Report",
            "Gemma 2: Improving Open Language Models at a Practical Size",
        ],
    },

    {
        "question": "Recent work on inference optimization",
        "route": "recent_developments",
        "expected_docs": [
            "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision",
            "The Era of 1-bit LLMs (BitNet b1.58)",
        ],
    },

    # ==================================================
    # FIND PAPERS (6)
    # ==================================================

    {
        "question": "Recommend papers on transformers",
        "route": "find_papers",
        "expected_docs": [
            "Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers",
            "Language Models are Few-Shot Learners",
        ],
    },

    {
        "question": "Recommend papers on RAG",
        "route": "find_papers",
        "expected_docs": [
            "Retrieval-Augmented Generation for Knowledge-Intensive NLP",
            "Corrective RAG (CRAG)",
            "From Local to Global: A Graph RAG Approach",
        ],
    },

    {
        "question": "Recommend papers on alignment",
        "route": "find_papers",
        "expected_docs": [
            "Training Language Models to Follow Instructions",
            "Constitutional AI: Harmlessness from AI Feedback",
            "Self-Rewarding Language Models",
        ],
    },

    {
        "question": "Recommend papers on reasoning",
        "route": "find_papers",
        "expected_docs": [
            "Chain-of-Thought Prompting Elicits Reasoning in LLMs",
            "DeepSeek-R1: Incentivizing Reasoning Capability via RL",
        ],
    },

    {
        "question": "Recommend papers on agents",
        "route": "find_papers",
        "expected_docs": [
            "ReAct: Synergizing Reasoning and Acting in Language Models",
            "SWE-Agent: Agent–Computer Interfaces Enable Software Engineering LMs",
        ],
    },

    {
        "question": "Recommend papers on quantization",
        "route": "find_papers",
        "expected_docs": [
            "The Era of 1-bit LLMs (BitNet b1.58)",
        ],
    },

    # ==================================================
    # OUT OF SCOPE (6)
    # ==================================================

    {
        "question": "Bitcoin price today",
        "route": "out_of_scope",
        "expected_docs": [],
    },

    {
        "question": "Who won IPL yesterday?",
        "route": "out_of_scope",
        "expected_docs": [],
    },

    {
        "question": "Capital of France",
        "route": "out_of_scope",
        "expected_docs": [],
    },

    {
        "question": "Weather in Hyderabad",
        "route": "out_of_scope",
        "expected_docs": [],
    },

    {
        "question": "Virat Kohli ODI average",
        "route": "out_of_scope",
        "expected_docs": [],
    },

    {
        "question": "Best restaurants in Hyderabad",
        "route": "out_of_scope",
        "expected_docs": [],
    },
]
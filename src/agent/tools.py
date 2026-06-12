from datetime import datetime


KNOWN_PAPERS = {
    "attention is all you need":
    "Attention Is All You Need",

    "bert":
    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",

    "lora":
    "LoRA: Low-Rank Adaptation of Large Language Models",

    "react":
    "ReAct: Synergizing Reasoning and Acting in Language Models",

    "llama 2":
    "Llama 2: Open Foundation and Fine-Tuned Chat Models",

    "mixtral":
    "Mixtral of Experts",

    "deepseek-r1":
    "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",

    "qwen2":
"Qwen2 Technical Report",

"deepseek-v3":
"DeepSeek-V3 Technical Report",

"flashattention":
"FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision",

"graphrag":
"From Local to Global: A Graph RAG Approach to Query-Focused Summarization",

"crag":
"Corrective Retrieval Augmented Generation",

"gpt-3":
"Language Models are Few-Shot Learners",

"bitnet":
"The Era of 1-bit LLMs",

"simpo":
"SimPO: Simple Preference Optimization with a Reference-Free Reward",

"kto":
"KTO: Model Alignment as Prospect Theoretic Optimization",
}


def lookup_paper(
    query: str,
):

    query = query.lower()

    for key, value in KNOWN_PAPERS.items():

        if key in query:

            return value

    return None


def get_recent_year_cutoff():

    current_year = datetime.now().year

    return current_year - 1
import os

# Model configuration
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")  # Default to GPT-4
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-opus-20240229")

# Graph configuration
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "3"))  # Max retry iterations
REFLECTION_FLAG = os.getenv("REFLECTION_FLAG", "do not reflect")  # Options: "reflect", "do not reflect"

# Documentation path
DOC_PATH = "data/lcel_docs.txt"

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# LangSmith settings
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false").lower() == "true"
LANGSMITH_PROJECT_NAME = os.getenv("LANGSMITH_PROJECT_NAME", "langgraph-code-assistant")

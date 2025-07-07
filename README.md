# LangGraph Code Assistant Project

This project implements a code generation workflow using LangGraph, Retrieval-Augmented Generation (RAG), and self-correction. It leverages LangChain Expression Language (LCEL) to build a graph-based application for answering coding questions based on provided documentation.

## Project Structure

```
langgraph_code_assistant/
├── data/
│   └── lcel_docs.txt  # LCEL documentation (extracted from notebook)
├── src/
│   ├── components/
│   │   ├── code_generator.py  # Code generation logic
│   │   ├── code_checker.py    # Code checking logic
│   │   └── reflector.py       # Reflection logic
│   ├── graph/
│   │   └── workflow.py        # LangGraph workflow definition
│   ├── utils/
│   │   └── llm_utils.py       # LLM utilities (e.g., prompt construction)
│   ├── config.py              # Configuration settings
│   ├── main.py                # Entry point for running the application
│   └── eval.py                # Evaluation scripts
├── README.md                  # This file
└── requirements.txt           # Project dependencies
```

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd langgraph_code_assistant
    ```

2.  **Set up a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set API keys:**

    Set the `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` environment variables. You can do this by adding the following lines to your `.bashrc` or `.zshrc` file:

    ```bash
    export OPENAI_API_KEY="your_openai_api_key"
    export ANTHROPIC_API_KEY="your_anthropic_api_key"
    ```

    Or, you can set them directly in your terminal session:

    ```bash
    export OPENAI_API_KEY="your_openai_api_key"
    export ANTHROPIC_API_KEY="your_anthropic_api_key"
    ```

## Usage

1.  **Run the main script:**

    ```bash
    python src/main.py --question "How do I build a RAG chain in LCEL?"
    ```

    You can also specify the question directly in the script or through command-line arguments.

2.  **Run evaluation:**

    ```bash
    python src/eval.py
    ```

    Make sure you have set up LangSmith and cloned the public dataset as described in the original notebook.

## Configuration

The project can be configured using the `src/config.py` file. You can modify parameters such as:

*   `LLM_MODEL`: The language model to use (e.g., "gpt-4o-mini", "claude-3-opus-20240229").
*   `MAX_ITERATIONS`: The maximum number of iterations for the LangGraph workflow.
*   `REFLECTION_FLAG`: Whether to use reflection in the workflow ("reflect" or "do not reflect").

## Modules

*   **data**: Contains the LCEL documentation (`lcel_docs.txt`).
*   **src**: Contains the source code for the project.
    *   **components**: Contains the logic for code generation, code checking, and reflection.
    *   **graph**: Contains the LangGraph workflow definition.
    *   **utils**: Contains utility functions for working with LLMs.
    *   **config.py**: Defines configuration settings for the project.
    *   **main.py**: The entry point for running the application.
    *   **eval.py**: Contains evaluation scripts.

## Dependencies

The project depends on the following packages:

*   langchain
*   langchain\_community
*   langchain\_openai
*   langchain\_anthropic
*   langgraph
*   beautifulsoup4
*   langsmith
*   typing-extensions

These dependencies are listed in the `requirements.txt` file.

import logging
import sys

import langsmith
from langsmith.evaluation import evaluate
from langsmith.schemas import Example, Run

from src.components.code_checker import check_execution, check_import
from src.config import LLM_MODEL, REFLECTION_FLAG
from src.graph.workflow import app
from src.utils.llm_utils import code_gen_chain, concatenated_content

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

client = langsmith.Client()


def predict_base_case(example: dict):
    """Context stuffing"""
    solution = code_gen_chain.invoke(
        {"context": concatenated_content, "messages": [("user", example["question"])]}
    )
    return {"imports": solution.imports, "code": solution.code}


def predict_langgraph(example: dict):
    """LangGraph"""
    graph = app.invoke(
        {"messages": [("user", example["question"])], "iterations": 0, "error": ""}
    )
    solution = graph["generation"]
    return {"imports": solution.imports, "code": solution.code}


def main():
    # Evaluator
    code_evaluator = [check_import, check_execution]

    # Dataset
    dataset_name = "lcel-teacher-eval"

    # Run base case
    try:
        experiment_results_ = evaluate(
            predict_base_case,
            data=dataset_name,
            evaluators=code_evaluator,
            experiment_prefix=f"test-without-langgraph-{LLM_MODEL}",
            max_concurrency=2,
            metadata={
                "llm": LLM_MODEL,
            },
        )
    except Exception as e:
        logger.error(f"Error running base case evaluation: {e}")
        print("Please setup LangSmith")
        return

    # Run with langgraph
    try:
        experiment_results = evaluate(
            predict_langgraph,
            data=dataset_name,
            evaluators=code_evaluator,
            experiment_prefix=f"test-with-langgraph-{LLM_MODEL}-{REFLECTION_FLAG}",
            max_concurrency=2,
            metadata={
                "llm": LLM_MODEL,
                "feedback": REFLECTION_FLAG,
            },
        )
    except Exception as e:
        logger.error(f"Error running LangGraph evaluation: {e}")
        print("Please setup LangSmith")
        return

    logger.info("Evaluation complete.")


if __name__ == "__main__":
    main()

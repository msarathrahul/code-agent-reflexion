import argparse
import logging
import sys

from src.config import MAX_ITERATIONS, REFLECTION_FLAG
from src.graph.workflow import app

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


def main(question: str):
    """
    Main function to run the LangGraph code assistant.

    Args:
        question (str): The coding question to answer.
    """
    logger.info(f"Starting LangGraph code assistant with question: {question}")

    try:
        solution = app.invoke({"messages": [("user", question)], "iterations": 0, "error": ""})
        logger.info("Code generation complete.")
        print(solution["generation"])  # Output the final solution
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LangGraph Code Assistant")
    parser.add_argument("--question", type=str, required=True, help="The coding question to answer")
    args = parser.parse_args()

    main(args.question)

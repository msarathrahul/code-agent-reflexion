import logging
import sys

from src.utils.llm_utils import code_gen_chain, concatenated_content

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_code(messages: list):
    """
    Generate a code solution

    Args:
        messages (list): List of messages in the conversation.

    Returns:
        Code: A code solution.
    """
    logger.info("Generating code solution...")
    code_solution = code_gen_chain.invoke(
        {"context": concatenated_content, "messages": messages}
    )
    logger.info("Code solution generated.")
    return code_solution

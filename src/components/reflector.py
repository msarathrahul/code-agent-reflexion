import logging
import sys

from src.utils.llm_utils import code_gen_chain, concatenated_content

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


def reflect_on_errors(messages: list):
    """
    Reflect on errors

    Args:
        messages (list): The current list of messages.

    Returns:
        str: Reflections on the error.
    """
    logger.info("Reflecting on errors...")
    reflections = code_gen_chain.invoke(
        {"context": concatenated_content, "messages": messages}
    )
    logger.info("Reflections generated.")
    return reflections

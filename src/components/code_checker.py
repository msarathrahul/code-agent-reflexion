import logging
import sys

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


def check_import(run, example) -> dict:
    imports = run.outputs.get("imports")
    try:
        exec(imports)
        return {"key": "import_check", "score": 1}
    except Exception:
        return {"key": "import_check", "score": 0}


def check_execution(run, example) -> dict:
    imports = run.outputs.get("imports")
    code = run.outputs.get("code")
    try:
        exec(imports + "\n" + code)
        return {"key": "code_execution_check", "score": 1}
    except Exception:
        return {"key": "code_execution_check", "score": 0}


def check_code(imports: str, code: str) -> str:
    """
    Check code for import and execution errors.

    Args:
        imports (str): The import statements.
        code (str): The code block.

    Returns:
        str: "no" if no errors, "yes" if errors.
    """
    logger.info("Checking code...")
    try:
        exec(imports)
    except Exception as e:
        logger.error(f"Code import check failed: {e}")
        return "yes"

    try:
        exec(imports + "\n" + code)
    except Exception as e:
        logger.error(f"Code execution check failed: {e}")
        return "yes"

    logger.info("No code test failures.")
    return "no"

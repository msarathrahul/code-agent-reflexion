import logging
import sys
from typing import List

from langgraph.graph import END, StateGraph, START
from typing_extensions import TypedDict

from components.code_checker import check_code
from components.code_generator import generate_code
from components.reflector import reflect_on_errors
from config import MAX_ITERATIONS, REFLECTION_FLAG

# ...existing code...
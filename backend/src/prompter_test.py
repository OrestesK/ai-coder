import unittest
import logging
from src.prompter import build_state_graph


class TestPrompter(unittest.TestCase):
    def test_prompter(self):
        graph = build_state_graph()
        input = {
            "code": """
        # Define state for application
        class State(TypedDict):
            code: str
            language: str
            context: List[Document]
            answer: str
        """,
            "language": "python",
        }
        try:
            res = graph.invoke(input)
            self.assertIsNotNone(res["answer"])
            logging.info(f"Prompter test passed: {res['answer']}")
        except Exception as e:
            self.fail(f"Prompter test failed with an exception: {e}")

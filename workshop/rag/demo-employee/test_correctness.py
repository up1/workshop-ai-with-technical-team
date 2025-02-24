import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams
import json

# Load test cases once at module level
with open('test_cases.json', 'r') as f:
    LOADED_CASES = json.load(f)

@pytest.fixture
def correctness_metric():
    return GEval(
        name="Correctness",
        model="gpt-4o",
        evaluation_params=[
            LLMTestCaseParams.EXPECTED_OUTPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT],
        evaluation_steps=[
            "Check whether the facts in 'actual output' contradicts any facts in 'expected output'",
            "You should also lightly penalize omission of detail, and focus on the main idea",
            "Vague language, or contradicting OPINIONS, are OK"
        ],
    )

@pytest.mark.parametrize("test_case_data", LOADED_CASES)
def test_correctness(test_case_data, correctness_metric):
    test_case = LLMTestCase(**test_case_data)
    assert_test(test_case, [correctness_metric])
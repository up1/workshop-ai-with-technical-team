from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams


def test_relevancy():
    correctness_metric = GEval(
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
    test_case_1 = LLMTestCase(
        input="Who is the CEO of the company?",
        actual_output="Grace Kim is the CEO of the company.",
        expected_output="Grace Kim",
        retrieval_context=[
            "Employee information \nGrace Kim is a CEO in the Executive department and working at Paris Office."
        ],
    )

    test_case_2 = LLMTestCase(
        input="Who is the CTO of the company?",
        actual_output="Frank Chen is the CTO of the company.",
        expected_output="Frank Chen",
        retrieval_context=[
            "Employee information \nFrank Chen is a CTO in the Executive department and working at San Francisco Office.",
        ],
    )
    assert_test(test_case_1, [correctness_metric])
    assert_test(test_case_2, [correctness_metric])
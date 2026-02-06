import pytest

from src.declare.constraints import AlternateResponse


@pytest.fixture
def alternate_response_constraint():
    return AlternateResponse("a", "b")


# --- Original Single Item Tests ---
def test_alternate_response_satisfying_example_1(alternate_response_constraint):
    trace = ["c", "a", "c", "b"]
    assert alternate_response_constraint.is_satisfied(trace) is True


def test_alternate_response_satisfying_example_2(alternate_response_constraint):
    trace = ["a", "b", "c", "a", "c", "b"]
    assert alternate_response_constraint.is_satisfied(trace) is True


def test_alternate_response_violating_example_1(alternate_response_constraint):
    trace = ["c", "a", "a", "c", "b"]
    assert alternate_response_constraint.is_satisfied(trace) is False


def test_alternate_response_violating_example_2(alternate_response_constraint):
    trace = ["b", "a", "c", "a", "c", "b"]
    assert alternate_response_constraint.is_satisfied(trace) is False

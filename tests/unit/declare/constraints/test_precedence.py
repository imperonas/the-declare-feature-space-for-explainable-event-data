import pytest

from src.declare.constraints import Precedence


@pytest.fixture
def precedence_constraint():
    return Precedence("a", "b")


# --- Original Single Item Tests ---
def test_precedence_satisfying_example_1(precedence_constraint):
    trace = ["c", "a", "c", "b", "b"]
    assert precedence_constraint.is_satisfied(trace) is True


def test_precedence_satisfying_example_2(precedence_constraint):
    trace = ["a", "c", "c"]
    assert precedence_constraint.is_satisfied(trace) is True


def test_precedence_violating_example_1(precedence_constraint):
    trace = ["c", "c", "b", "b"]
    assert precedence_constraint.is_satisfied(trace) is False


def test_precedence_violating_example_2(precedence_constraint):
    trace = ["b", "a", "c", "c"]
    assert precedence_constraint.is_satisfied(trace) is False

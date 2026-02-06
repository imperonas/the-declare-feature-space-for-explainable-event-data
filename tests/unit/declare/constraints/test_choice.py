import pytest

from src.declare.constraints import Choice


@pytest.fixture
def choice_constraint():
    return Choice("a", "b")


# --- Original Single Item Tests ---
def test_choice_satisfying_example_1(choice_constraint):
    trace = ["a", "c", "d"]
    assert choice_constraint.is_satisfied(trace) is True


def test_choice_satisfying_example_2(choice_constraint):
    trace = ["c", "b", "d"]
    assert choice_constraint.is_satisfied(trace) is True


def test_choice_satisfying_example_3(choice_constraint):
    trace = ["a", "b", "c"]
    assert choice_constraint.is_satisfied(trace) is True


def test_choice_violating_example_1(choice_constraint):
    trace = ["c", "d", "e"]
    assert choice_constraint.is_satisfied(trace) is False


def test_choice_violating_example_2(choice_constraint):
    trace = ["x", "y"]
    assert choice_constraint.is_satisfied(trace) is False

import pytest

from src.declare.constraints import ExclusiveChoice


@pytest.fixture
def exclusive_choice_constraint():
    return ExclusiveChoice("a", "b")


# --- Original Single Item Tests ---
def test_exclusive_choice_satisfying_example_1(exclusive_choice_constraint):
    trace = ["a", "c", "d"]
    assert exclusive_choice_constraint.is_satisfied(trace) is True


def test_exclusive_choice_satisfying_example_2(exclusive_choice_constraint):
    trace = ["c", "b", "d"]
    assert exclusive_choice_constraint.is_satisfied(trace) is True


def test_exclusive_choice_violating_example_1(exclusive_choice_constraint):
    trace = ["a", "b", "c"]
    assert exclusive_choice_constraint.is_satisfied(trace) is False


def test_exclusive_choice_violating_example_2(exclusive_choice_constraint):
    trace = ["c", "d", "e"]
    assert exclusive_choice_constraint.is_satisfied(trace) is False


def test_exclusive_choice_violating_example_3(exclusive_choice_constraint):
    trace = ["x", "y"]
    assert exclusive_choice_constraint.is_satisfied(trace) is False

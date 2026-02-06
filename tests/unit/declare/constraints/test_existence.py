import pytest

from src.declare.constraints import Existence


@pytest.fixture
def existence_constraint():
    return Existence("a")


# --- Original Single Item Tests ---
def test_existence_satisfying_example_1(existence_constraint):
    trace = ["b", "c", "a", "c"]
    assert existence_constraint.is_satisfied(trace) is True


def test_existence_satisfying_example_2(existence_constraint):
    trace = ["b", "c", "a", "a", "c"]
    assert existence_constraint.is_satisfied(trace) is True


def test_existence_violating_example_1(existence_constraint):
    trace = ["b", "c", "c"]
    assert existence_constraint.is_satisfied(trace) is False


def test_existence_violating_example_2(existence_constraint):
    trace = ["c"]
    assert existence_constraint.is_satisfied(trace) is False

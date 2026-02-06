import pytest

from src.declare.constraints import NotCoexistence


@pytest.fixture
def not_coexistence_constraint():
    return NotCoexistence("a", "b")


# --- Original Single Item Tests ---
def test_not_coexistence_satisfying_example_1(not_coexistence_constraint):
    trace = ["c", "c", "c", "b", "b", "b"]
    assert not_coexistence_constraint.is_satisfied(trace) is True


def test_not_coexistence_satisfying_example_2(not_coexistence_constraint):
    trace = ["c", "c", "a", "c"]
    assert not_coexistence_constraint.is_satisfied(trace) is True


def test_not_coexistence_violating_example_1(not_coexistence_constraint):
    trace = ["a", "c", "c", "b", "b"]
    assert not_coexistence_constraint.is_satisfied(trace) is False


def test_not_coexistence_violating_example_2(not_coexistence_constraint):
    trace = ["b", "c", "a", "c"]
    assert not_coexistence_constraint.is_satisfied(trace) is False

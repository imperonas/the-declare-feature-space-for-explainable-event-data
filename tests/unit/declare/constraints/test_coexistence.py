import pytest

from src.declare.constraints import CoExistence


@pytest.fixture
def coexistence_constraint():
    return CoExistence("a", "b")


# --- Original Single Item Tests ---
def test_coexistence_satisfying_example_1(coexistence_constraint):
    trace = ["c", "a", "c", "b", "b"]
    assert coexistence_constraint.is_satisfied(trace) is True


def test_coexistence_satisfying_example_2(coexistence_constraint):
    trace = ["b", "c", "c", "a"]
    assert coexistence_constraint.is_satisfied(trace) is True


def test_coexistence_violating_example_1(coexistence_constraint):
    trace = ["c", "a", "c"]
    assert coexistence_constraint.is_satisfied(trace) is False


def test_coexistence_violating_example_2(coexistence_constraint):
    trace = ["b", "c", "c"]
    assert coexistence_constraint.is_satisfied(trace) is False

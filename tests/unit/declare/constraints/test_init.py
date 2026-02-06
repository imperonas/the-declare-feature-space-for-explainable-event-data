import pytest

from src.declare.constraints.unaray_constraints import Init


@pytest.fixture
def init_constraint():
    return Init("a")


# --- Original Single Item Tests ---
def test_init_satisfying_example_1(init_constraint):
    trace = ["a", "c", "c"]
    assert init_constraint.is_satisfied(trace) is True


def test_init_satisfying_example_2(init_constraint):
    trace = ["a", "b", "a", "c"]
    assert init_constraint.is_satisfied(trace) is True


def test_init_violating_example_1(init_constraint):
    trace = ["c", "c"]
    assert init_constraint.is_satisfied(trace) is False


def test_init_violating_example_2(init_constraint):
    trace = ["b", "a", "c"]
    assert init_constraint.is_satisfied(trace) is False

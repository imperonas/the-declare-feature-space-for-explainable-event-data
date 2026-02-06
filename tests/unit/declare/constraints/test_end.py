import pytest

from src.declare.constraints import End


@pytest.fixture
def end_constraint():
    return End("a")


# --- Original Single Item Tests ---
def test_end_satisfying_example_1(end_constraint):
    trace = ["b", "c", "a"]
    assert end_constraint.is_satisfied(trace) is True


def test_end_satisfying_example_2(end_constraint):
    trace = ["b", "a", "c", "a"]
    assert end_constraint.is_satisfied(trace) is True


def test_end_violating_example_1(end_constraint):
    trace = ["b", "c"]
    assert end_constraint.is_satisfied(trace) is False


def test_end_violating_example_2(end_constraint):
    trace = ["b", "a", "c"]
    assert end_constraint.is_satisfied(trace) is False

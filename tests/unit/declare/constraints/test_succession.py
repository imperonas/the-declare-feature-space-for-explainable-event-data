import pytest

from src.declare.constraints import Succession


@pytest.fixture
def succession_constraint():
    return Succession("a", "b")


# --- Original Single Item Tests ---
def test_succession_satisfying_example_1(succession_constraint):
    trace = ["c", "a", "c", "b", "b"]
    assert succession_constraint.is_satisfied(trace) is True


def test_succession_satisfying_example_2(succession_constraint):
    trace = ["a", "c", "c", "b"]
    assert succession_constraint.is_satisfied(trace) is True


def test_succession_violating_example_1(succession_constraint):
    trace = ["b", "a", "c"]
    assert succession_constraint.is_satisfied(trace) is False


def test_succession_violating_example_2(succession_constraint):
    trace = ["b", "c", "c", "a"]
    assert succession_constraint.is_satisfied(trace) is False

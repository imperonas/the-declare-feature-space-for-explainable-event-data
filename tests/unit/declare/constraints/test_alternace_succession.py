import pytest

from src.declare.constraints import AlternateSuccession


@pytest.fixture
def alternate_succession_constraint():
    return AlternateSuccession("a", "b")


# --- Original Single Item Tests ---
def test_alternate_succession_satisfying_example_1(alternate_succession_constraint):
    trace = ["c", "a", "c", "b", "a", "b"]
    assert alternate_succession_constraint.is_satisfied(trace) is True


def test_alternate_succession_satisfying_example_2(alternate_succession_constraint):
    trace = ["a", "b", "c", "a", "b", "c"]
    assert alternate_succession_constraint.is_satisfied(trace) is True


def test_alternate_succession_violating_example_1(alternate_succession_constraint):
    trace = ["c", "a", "a", "c", "b", "b"]
    assert alternate_succession_constraint.is_satisfied(trace) is False


def test_alternate_succession_violating_example_2(alternate_succession_constraint):
    trace = ["b", "a", "c"]
    assert alternate_succession_constraint.is_satisfied(trace) is False

import pytest

from src.declare.constraints import AlternatePrecedence


@pytest.fixture
def alternate_precedence_constraint():
    return AlternatePrecedence("a", "b")


# --- Original Single Item Tests ---
def test_alternate_precedence_satisfying_example_1(alternate_precedence_constraint):
    trace = ["c", "a", "c", "b", "a"]
    assert alternate_precedence_constraint.is_satisfied(trace) is True


def test_alternate_precedence_satisfying_example_2(alternate_precedence_constraint):
    trace = ["a", "b", "c", "a", "a", "c", "b"]
    assert alternate_precedence_constraint.is_satisfied(trace) is True


def test_alternate_precedence_violating_example_1(alternate_precedence_constraint):
    trace = ["c", "a", "c", "b", "b", "a"]
    assert alternate_precedence_constraint.is_satisfied(trace) is False


def test_alternate_precedence_violating_example_2(alternate_precedence_constraint):
    trace = ["a", "b", "b", "a", "b", "c", "b"]
    assert alternate_precedence_constraint.is_satisfied(trace) is False

import pytest

from src.declare.constraints import ChainPrecedence


@pytest.fixture
def chain_precedence_constraint():
    return ChainPrecedence("a", "b")


# --- Original Single Item Tests ---
def test_chain_precedence_satisfying_example_1(chain_precedence_constraint):
    trace = ["a", "b", "c", "a"]
    assert chain_precedence_constraint.is_satisfied(trace) is True


def test_chain_precedence_satisfying_example_2(chain_precedence_constraint):
    trace = ["a", "b", "a", "a", "b", "c"]
    assert chain_precedence_constraint.is_satisfied(trace) is True


def test_chain_precedence_violating_example_1(chain_precedence_constraint):
    trace = ["b", "c", "a"]
    assert chain_precedence_constraint.is_satisfied(trace) is False


def test_chain_precedence_violating_example_2(chain_precedence_constraint):
    trace = ["b", "a", "a", "c", "b"]
    assert chain_precedence_constraint.is_satisfied(trace) is False

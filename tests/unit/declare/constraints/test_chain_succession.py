import pytest

from src.declare.constraints import ChainSuccession


@pytest.fixture
def chain_succession_constraint():
    return ChainSuccession("a", "b")


# --- Original Single Item Tests ---
def test_chain_succession_satisfying_example_1(chain_succession_constraint):
    trace = ["c", "a", "b", "a", "b"]
    assert chain_succession_constraint.is_satisfied(trace) is True


def test_chain_succession_satisfying_example_2(chain_succession_constraint):
    trace = ["c", "c", "c"]
    assert chain_succession_constraint.is_satisfied(trace) is True


def test_chain_succession_violating_example_1(chain_succession_constraint):
    trace = ["c", "a", "c", "b"]
    assert chain_succession_constraint.is_satisfied(trace) is False


def test_chain_succession_violating_example_2(chain_succession_constraint):
    trace = ["c", "b", "a", "c"]
    assert chain_succession_constraint.is_satisfied(trace) is False

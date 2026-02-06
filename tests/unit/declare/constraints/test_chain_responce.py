import pytest

from src.declare.constraints import ChainResponse


@pytest.fixture
def chain_response_constraint():
    return ChainResponse("a", "b")


# --- Original Single Item Tests ---
def test_chain_response_satisfying_example_1(chain_response_constraint):
    trace = ["c", "a", "b", "b"]
    assert chain_response_constraint.is_satisfied(trace) is True


def test_chain_response_satisfying_example_2(chain_response_constraint):
    trace = ["a", "b", "c", "a", "b"]
    assert chain_response_constraint.is_satisfied(trace) is True


def test_chain_response_violating_example_1(chain_response_constraint):
    trace = ["c", "a", "c", "b"]
    assert chain_response_constraint.is_satisfied(trace) is False


def test_chain_response_violating_example_2(chain_response_constraint):
    trace = ["b", "c", "a"]
    assert chain_response_constraint.is_satisfied(trace) is False

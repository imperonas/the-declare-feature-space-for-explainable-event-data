import pytest

from src.declare.constraints import Response


@pytest.fixture
def response_constraint():
    return Response(activation="a", target="b")


@pytest.fixture
def response_sets():
    # Any of {a,b} must be followed by one of {c,d}
    return Response(activation=["a", "b"], target=["c", "d"])


def create_trace(activities):
    return [{"concept:name": act} for act in activities]


# --- Original Single Item Tests ---
def test_response_satisfying_example_1(response_constraint):
    trace = ["c", "a", "a", "c", "b"]
    assert response_constraint.is_satisfied(trace) is True


def test_response_satisfying_example_2(response_constraint):
    trace = ["b", "c", "c"]
    assert response_constraint.is_satisfied(trace) is True


def test_response_violating_example_1(response_constraint):
    trace = ["c", "a", "a", "c"]
    assert response_constraint.is_satisfied(trace) is False


def test_response_violating_example_2(response_constraint):
    trace = ["b", "a", "c", "c"]
    assert response_constraint.is_satisfied(trace) is False

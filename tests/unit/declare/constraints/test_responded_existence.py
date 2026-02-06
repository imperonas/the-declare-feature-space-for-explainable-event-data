import pytest

from src.declare.constraints import RespondedExistence


@pytest.fixture
def responded_existence_constraint():
    # Table: RespondedExistence(a, b): if a then b
    # Implementation logic: if target exists, activation must exist
    # So: RespondedExistence(activation="b", target="a") -> If "a" exists, "b" must exist
    return RespondedExistence("b", "a")


# --- Original Single Item Tests ---
def test_responded_existence_satisfying_example_1(responded_existence_constraint):
    trace = ["b", "c", "a", "a", "c"]
    assert responded_existence_constraint.is_satisfied(trace) is True


def test_responded_existence_satisfying_example_2(responded_existence_constraint):
    trace = ["b", "c", "c"]
    assert responded_existence_constraint.is_satisfied(trace) is True


def test_responded_existence_violating_example_1(responded_existence_constraint):
    trace = ["c", "a", "a", "c"]
    assert responded_existence_constraint.is_satisfied(trace) is False


def test_responded_existence_violating_example_2(responded_existence_constraint):
    trace = ["a", "c", "c"]
    assert responded_existence_constraint.is_satisfied(trace) is False

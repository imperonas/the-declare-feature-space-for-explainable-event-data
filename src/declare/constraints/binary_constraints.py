from abc import ABC, abstractmethod

from .declare import DeclareConstraint


class BinaryDeclareConstraint(DeclareConstraint):
    def __init__(self, activation, target):
        self.activation = activation
        self.target = target

    @abstractmethod
    def is_satisfied(self, x):
        pass


# region Response
class Response(BinaryDeclareConstraint):
    """
    Response constraint: If activation occurs, ONE OF the target activities must eventually follow.
    """

    def is_satisfied(self, x):
        for i, a in enumerate(x):
            # if current activity is activation
            if a == self.activation:
                # Check if ANY target exists in the remainder of the trace
                if not self.target in x[i + 1 :]:
                    return False
        return True

    def __str__(self):
        return f"Response({self.activation}, {self.target})"


class ChainResponse(BinaryDeclareConstraint):
    """Chain Response: Activation must be immediately followed by Target."""

    def is_satisfied(self, x):
        # Check all but the last event
        for i, act in enumerate(x[:-1]):
            if act == self.activation:
                # Next event MUST be in target set
                if x[i + 1] != self.target:
                    return False

        # Check the last event - if it's activation, it's a violation (nothing follows it)
        if x[-1] == self.activation:
            return False
        return True

    def __str__(self):
        return f"ChainResponse({self.activation}, {self.target})"


class AlternateResponse(BinaryDeclareConstraint):
    """Alternate Response: Each activation must be followed by exactly one target before next activation."""

    def is_satisfied(self, x):
        awaiting_target = False

        for act in x:
            if act == self.activation:
                if awaiting_target:
                    return False  # found another activation before target was satisfied
                awaiting_target = True
            elif act == self.target and awaiting_target:
                awaiting_target = False

        return not awaiting_target

    def __str__(self):
        return f"AlternateResponse({self.activation}, {self.target})"


class RespondedExistence(BinaryDeclareConstraint):
    """
    Responded Existence: If target occurs, activation must also occur somewhere.
    """

    def is_satisfied(self, x):
        target_present = self.target in x

        if target_present:
            # Then ANY activation must be present
            return self.activation in x
        return True

    def __str__(self):
        return f"RespondedExistence({self.activation}, {self.target})"


# endregion


# region Precedence
class Precedence(BinaryDeclareConstraint):
    """
    Precedence: Target can only occur after activation has occurred.
    """

    def is_satisfied(self, x):
        for i, a in enumerate(x):
            # If current event is a target
            if a == self.target:
                # Check if ANY activation occurred before this index
                if not self.activation in x[:i]:
                    return False
        return True

    def __str__(self):
        return f"Precedence({self.activation}, {self.target})"


class ChainPrecedence(BinaryDeclareConstraint):
    """Chain Precedence: Target must be immediately preceded by Activation."""

    def is_satisfied(self, x):
        # Check all but the first event
        for i, act in enumerate(x[1:], start=1):
            if act == self.target:
                # Previous event MUST be in activation set
                if x[i - 1] != self.activation:
                    return False

        # Check the first event - if it's target, it's a violation (nothing precedes it)
        if x[0] == self.target:
            return False
        return True

    def __str__(self):
        return f"ChainPrecedence({self.activation}, {self.target})"


class AlternatePrecedence(BinaryDeclareConstraint):
    """Alternate Precedence: Each target must be preceded by exactly one activation, alternating."""

    def is_satisfied(self, x):
        has_pending_activation = False

        for act in x:
            if act == self.activation:
                has_pending_activation = True
            elif act == self.target:
                if not has_pending_activation:
                    return False  # Target appears without preceding activation or double target
                has_pending_activation = False  # Consume the activation
        return True

    def __str__(self):
        return f"AlternatePrecedence({self.activation}, {self.target})"


# endregion


# region Succession
class Succession(BinaryDeclareConstraint):
    """
    Succession: Combines Response and Precedence.
    """

    def __init__(self, activation, target):
        super().__init__(activation, target)

        self.response = Response(activation, target)
        self.precedence = Precedence(activation, target)

    def is_satisfied(self, x):
        return self.response.is_satisfied(x) and self.precedence.is_satisfied(x)

    def __str__(self):
        return f"Succession({self.activation}, {self.target})"


class ChainSuccession(BinaryDeclareConstraint):
    """Chain Succession: Strict immediate sequence."""

    def __init__(self, activation, target):
        super().__init__(activation, target)
        self.chain_response = ChainResponse(activation, target)
        self.chain_precedence = ChainPrecedence(activation, target)

    def is_satisfied(self, x):
        return self.chain_response.is_satisfied(
            x
        ) and self.chain_precedence.is_satisfied(x)

    def __str__(self):
        return f"ChainSuccession({self.activation}, {self.target})"


class AlternateSuccession(BinaryDeclareConstraint):
    """Alternate Succession."""

    def __init__(self, activation, target):
        super().__init__(activation, target)
        self.response = AlternateResponse(activation, target)
        self.precedence = AlternatePrecedence(activation, target)

    def is_satisfied(self, x):
        return self.response.is_satisfied(x) and self.precedence.is_satisfied(x)

    def __str__(self):
        return f"AlternateSuccession({self.activation}, {self.target})"


# endregion


# region Choice
class Choice(BinaryDeclareConstraint):
    """At least one of the activities (from set 1 or set 2) must occur."""

    def is_satisfied(self, x):
        a_present = self.activation in x
        t_present = self.target in x
        return a_present or t_present

    def __str__(self):
        return f"Choice({self.activation}, {self.target})"


class ExclusiveChoice(BinaryDeclareConstraint):
    """Exactly one of the two sets of activities must occur (XOR logic on sets)."""

    def is_satisfied(self, x):
        a_present = self.activation in x
        t_present = self.target in x
        return (a_present and not t_present) or (t_present and not a_present)

    def __str__(self):
        return f"ExclusiveChoice({self.activation}, {self.target})"


# endregion


# region CoExistence
class CoExistence(BinaryDeclareConstraint):
    """If one activation activity occurs, a target activity must also occur."""

    def is_satisfied(self, x):
        a_present = self.activation in x
        t_present = self.target in x
        # Both present OR both absent
        return (a_present and t_present) or (not a_present and not t_present)

    def __str__(self):
        return f"CoExistence({self.activation}, {self.target})"


class NotCoexistence(BinaryDeclareConstraint):
    """Activities from set 1 and set 2 cannot both appear in the trace."""

    def is_satisfied(self, x):
        a_present = self.activation in x
        t_present = self.target in x
        return not (a_present and t_present)

    def __str__(self):
        return f"NotCoexistence({self.activation}, {self.target})"


# endregion

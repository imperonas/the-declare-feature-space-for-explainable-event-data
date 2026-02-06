from abc import ABC, abstractmethod
from typing import List

import numpy as np


class DeclareConstraint(ABC):
    @abstractmethod
    def is_satisfied(self, x: np.ndarray) -> bool:
        pass


class NegatedDeclareConstraint(DeclareConstraint):
    """Logically negates any other constraint (NOT)"""

    def __init__(self, constraint: DeclareConstraint):
        self.constraint = constraint

    def is_satisfied(self, x):
        return not self.constraint.is_satisfied(x)

    def __str__(self):
        return f"NOT {str(self.constraint)}"


class ConjunctiveDeclareConstraint(DeclareConstraint):
    """Combines constraints with AND logic"""

    def __init__(self, constraints: List[DeclareConstraint]):
        self.constraints = constraints

    def is_satisfied(self, x):
        return all([c.is_satisfied(x) for c in self.constraints])

    def __str__(self):
        return f"({' AND '.join(str(c) for c in self.constraints)})"


class DisjunctiveDeclareConstraint(DeclareConstraint):
    """Combines constraints with OR logic"""

    def __init__(self, constraints: List[DeclareConstraint]):
        self.constraints = constraints

    def is_satisfied(self, x):
        return any([c.is_satisfied(x) for c in self.constraints])

    def __str__(self):
        return f"({' OR '.join(str(c) for c in self.constraints)})"

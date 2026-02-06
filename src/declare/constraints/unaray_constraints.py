from abc import ABC, abstractmethod

import numpy as np

from .declare import DeclareConstraint


class UnaryDeclareConstraint(DeclareConstraint):

    def __init__(self, activity: any):
        self.activity = activity

    @abstractmethod
    def is_satisfied(self, x):
        pass


class Existence(UnaryDeclareConstraint):
    """Checks if an activity is present"""

    def is_satisfied(self, x: np.ndarray):
        return self.activity in x

    def __str__(self):
        return f"Existence({self.activity})"


class Absence(UnaryDeclareConstraint):
    """Checks if an activity is absent, inverse of Existence"""

    def __init__(self, activity):
        super().__init__(activity)
        self.existence = Existence(activity)

    def is_satisfied(self, x: np.ndarray):
        return not self.existence.is_satisfied(x)

    def __str__(self):
        return f"Absence({self.activity})"


class Init(UnaryDeclareConstraint):
    """Checks if a trace starts with a given activity"""

    def is_satisfied(self, x: np.ndarray):
        return self.activity == x[0]

    def __str__(self):
        return f"Init({self.activity})"


class End(UnaryDeclareConstraint):
    """Checks if a trace ends with a given activity"""

    def is_satisfied(self, x: np.ndarray):
        return self.activity == x[-1]

    def __str__(self):
        return f"End({self.activity})"

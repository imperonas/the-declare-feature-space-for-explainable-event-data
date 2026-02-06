from abc import ABC, abstractmethod
from typing import List

import numpy as np
import pandas as pd
from numpy.typing import NDArray

from src.declare.constraints.declare import DeclareConstraint
from src.feature_space.abstract_space import AbstractInterpretableSpace


class DeclarativeFeatureSpace(AbstractInterpretableSpace):
    def __init__(self, constraints: List[DeclareConstraint]):
        self.constraints = constraints

    def to_interpretable_instance(self, x: np.ndarray) -> NDArray[np.bool_]:
        interpretable_space = np.array([], dtype=bool)
        for constraint in self.constraints:
            is_satisfied = constraint.is_satisfied(x)
            interpretable_space = np.append(interpretable_space, is_satisfied)
        return interpretable_space

    def get_features(self):
        return [str(c) for c in self.constraints]

    def represent_instance(self, x: NDArray[np.bool_]) -> str:
        result = []
        for i, constraint in enumerate(self.constraints):
            if x[i]:
                result.append(str(constraint))
            else:
                result.append(f"NOT {constraint}")
        return ", ".join(result)

    def represent_matrix(self, X: NDArray[np.bool_]) -> pd.DataFrame:
        constraint_names = [str(constraint) for constraint in self.constraints]
        return pd.DataFrame(X, columns=constraint_names)

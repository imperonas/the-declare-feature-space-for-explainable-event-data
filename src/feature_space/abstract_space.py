from abc import ABC, abstractmethod
from typing import List

import numpy as np
import pandas as pd
from numpy.typing import NDArray


class AbstractInterpretableSpace(ABC):
    @abstractmethod
    def to_interpretable_instance(self, x: np.ndarray) -> NDArray[np.bool_]:  # x -> z
        pass

    def to_interpretable_set(self, X: np.ndarray) -> NDArray[np.bool_]:  # X -> Z
        return np.array([self.to_interpretable_instance(x) for x in X])

    @abstractmethod
    def get_features(self) -> List[str]:
        pass

    def represent_instance(self, x: NDArray[np.bool_]) -> str:
        pass

    def represent_matrix(self, X: NDArray[np.bool_]) -> pd.DataFrame:
        pass

import numpy as np


def one_hot(indices, num_classes) -> np.ndarray:
    """:return: A one-hot encoded vector."""
    vec = np.zeros((num_classes,), dtype=np.int64)
    vec[indices] = 1
    return vec

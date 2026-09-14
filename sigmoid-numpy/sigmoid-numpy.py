import math
import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    if isinstance(x, list):
        data = np.array(x)
        return 1/(1+np.exp(-data))
    else:
        return 1/(1+math.exp(-x))
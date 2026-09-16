import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    match method:
        case "zeros":
            return torch.zeros(shape)
        case "ones":
            return torch.ones(shape)
        case "full":
            return torch.full(shape, value)
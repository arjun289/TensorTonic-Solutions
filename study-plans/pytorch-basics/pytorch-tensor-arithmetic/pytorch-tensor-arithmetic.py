import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    x = torch.tensor(x)
    y = torch.tensor(y)
    match op:
        case "add":
            return torch.add(x, y).tolist()
        case "multiply":
            return torch.mul(x,y).tolist()
        case "matmul":
            dot_product = x @ y
            return dot_product.tolist()
        case "power":
            return torch.pow(x,y).tolist()
        case "max":
            return torch.max(x,y).tolist()
            
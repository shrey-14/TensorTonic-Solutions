import torch

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Returns the scaled dot-product attention output.
    """
    wei = (Q @ K.transpose(-2, -1)) / (K.shape[-1] ** 0.5)
    wei = torch.softmax(wei, dim=-1)
    return wei @ V
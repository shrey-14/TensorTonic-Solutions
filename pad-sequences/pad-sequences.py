import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if len(seqs) == 0:
        return np.empty((0, 0), dtype=int)
    if not max_len:
        max_len = max(len(seq) for seq in seqs)
    for i in range(len(seqs)):
        seqs[i] = seqs[i][:max_len]
        seqs[i].extend([pad_value] * (max_len - len(seqs[i])))

    return np.array(seqs, dtype=np.int64)
import math

def generate_anchors(feature_size: int, image_size: float, scales: list[float], aspect_ratios: list[float]) -> list[list[float]]:
    """
    Returns a list of [x1, y1, x2, y2] anchor boxes.
    """
    a_list = []
    s = image_size / feature_size
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5) * s
            cy = (i + 0.5) * s
            for scale in scales:
                for ar in aspect_ratios:
                    w = scale * math.sqrt(ar)
                    h = scale / math.sqrt(ar)

                    a_list.append([cx - w/2, cy - h/2, cx + w/2, cy + h/2])
        
    return a_list
            
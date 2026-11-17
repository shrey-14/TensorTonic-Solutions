import numpy as np

def color_to_grayscale(image: list) -> list:
    """
    Returns the luminance value of every RGB pixel.
    """
    # Write code here
    m,n,i = np.shape(image)
    gray = []
    for i in range(m):
        temp = []
        for j in range(n):
            img = image[i][j]
            temp.append(0.299*img[0]+0.587*img[1]+0.114*img[2])
        gray.append(temp)
    return gray
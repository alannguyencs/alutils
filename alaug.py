import numpy as np




def keep_aspect(sk_image):
    h, w, _ = sk_image.shape
    dim_diff = np.abs(h - w)
    # Upper (left) and lower (right) padding
    pad1, pad2 = dim_diff // 2, dim_diff - dim_diff // 2
    # Determine padding
    pad = ((pad1, pad2), (0, 0), (0, 0)) if h <= w else ((0, 0), (pad1, pad2), (0, 0))
    # Add padding
    aug_image = np.pad(sk_image, pad, 'constant', constant_values=0)

    return aug_image, pad
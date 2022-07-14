window_size = 840

def denormalize_x(x_norm):
    half_size = window_size/2
    if x_norm >= 0:
        return int((x_norm * half_size) + half_size)
    else:
        return int(half_size - (-x_norm * half_size))


def denormalize_y(y_norm):
    half_size = window_size/2
    if y_norm >= 0:
        return int(half_size - (y_norm * half_size))
    else:
        return int((-y_norm * half_size) + half_size)


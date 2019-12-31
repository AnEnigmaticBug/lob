def clamp(x, lower_bound, upper_bound):
    if x < lower_bound: return lower_bound
    if x > upper_bound: return upper_bound
    return x

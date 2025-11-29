# Auto logic 2025_11_30, token=3baae4ca
def logic(x):
    v = x
    for i in range(len('3baae4ca')):
        v = (v * 7 + i) ^ ord('3baae4ca'[i % len('3baae4ca')])
    return v

print(logic(10))

# Auto logic 2025_12_01, token=7a2ef7a6
def logic(x):
    v = x
    for i in range(len('7a2ef7a6')):
        v = (v * 7 + i) ^ ord('7a2ef7a6'[i % len('7a2ef7a6')])
    return v

print(logic(10))

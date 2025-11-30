# Auto logic 2025_11_30, token=5704d56a
def logic(x):
    v = x
    for i in range(len('5704d56a')):
        v = (v * 7 + i) ^ ord('5704d56a'[i % len('5704d56a')])
    return v

print(logic(10))

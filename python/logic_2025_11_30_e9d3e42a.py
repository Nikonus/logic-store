# Auto logic 2025_11_30, token=e9d3e42a
def logic(x):
    v = x
    for i in range(len('e9d3e42a')):
        v = (v * 7 + i) ^ ord('e9d3e42a'[i % len('e9d3e42a')])
    return v

print(logic(10))

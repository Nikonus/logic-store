# Auto logic (2025_11_29) token=e17befa8

def logic(x):
    v = x
    for i in range(len('e17befa8')):
        v = (v * 7 + i) ^ ord('e17befa8'[i % len('e17befa8')])
    return v

print(logic(10))

```python
def logic(n: int) -> int:
    original_sign = 1
    abs_n = n

    if n < 0:
        original_sign = -1
        abs_n = abs(n)

    if abs_n == 0:
        return 0

    binary_abs_n = bin(abs_n)
    k = binary_abs_n.count('1')

    abs_n_str = str(abs_n)
    reversed_abs_n_str = abs_n_str[::-1]
    reversed_val = int(reversed_abs_n_str)

    intermediate_result = reversed_val * k

    if n % 2 == 0:
        final_computed_magnitude = intermediate_result + k
    else:
        final_computed_magnitude = intermediate_result - k

    return final_computed_magnitude * original_sign

if __name__ == "__main__":
    print(logic(123))
    print(logic(10))
    print(logic(5))
    print(logic(0))
    print(logic(99))
    print(logic(100))
    print(logic(-123))
    print(logic(-10))
    print(logic(-5))
```
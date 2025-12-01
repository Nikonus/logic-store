```python
def logic(n):
    if n == 0:
        return 0

    abs_n = abs(n)
    s_abs_n = str(abs_n)

    sum_powers = sum(int(digit) ** (i + 1) for i, digit in enumerate(s_abs_n))

    shifted_abs_n = abs_n * (abs_n % 10 + 1)

    set_bits = bin(abs_n).count('1')

    intermediate_result = (sum_powers + shifted_abs_n)

    if n < 0:
        final_transform = intermediate_result - (set_bits * abs_n % 7)
    else:
        final_transform = intermediate_result * (set_bits + abs_n % 3)

    return final_transform

if __name__ == "__main__":
    print(f"logic(0) = {logic(0)}")
    print(f"logic(1) = {logic(1)}")
    print(f"logic(5) = {logic(5)}")
    print(f"logic(10) = {logic(10)}")
    print(f"logic(123) = {logic(123)}")
    print(f"logic(-1) = {logic(-1)}")
    print(f"logic(-5) = {logic(-5)}")
    print(f"logic(-10) = {logic(-10)}")
    print(f"logic(-123) = {logic(-123)}")
    print(f"logic(7) = {logic(7)}")
    print(f"logic(-7) = {logic(-7)}")
    print(f"logic(42) = {logic(42)}")
    print(f"logic(-100) = {logic(-100)}")
```
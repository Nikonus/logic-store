```python
import math

def logic(n):
    is_negative = n < 0
    abs_n = abs(n)

    if abs_n == 0:
        return 0

    binary_representation = bin(abs_n)[2:]
    reversed_binary_value = int(binary_representation[::-1], 2)

    set_bits_count = binary_representation.count('1')

    num_digits_base10 = int(math.log10(abs_n)) + 1

    transformed_value = reversed_binary_value + (set_bits_count * num_digits_base10)

    if is_negative:
        return -transformed_value
    else:
        return transformed_value

if __name__ == "__main__":
    test_numbers = [0, 1, 6, 7, 10, 15, 32, 100, -5, -123, 255]

    for num in test_numbers:
        result = logic(num)
        print(f"logic({num}) = {result}")
```
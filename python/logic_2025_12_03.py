```python
def logic(n):
    if n == 0:
        return 0

    seed_value = abs(n)
    digits_str = str(seed_value)
    transformed_value = seed_value

    for i, char_digit in enumerate(digits_str):
        digit = int(char_digit)
        position_index = i + 1

        if digit % 2 == 0:
            if position_index % 2 == 0:
                transformed_value = transformed_value + (digit * position_index) // 2
            else:
                transformed_value = transformed_value - (digit + position_index)
        else:
            if position_index % 2 == 0:
                transformed_value = transformed_value * digit + position_index
            else:
                divisor = digit + position_index
                transformed_value = transformed_value // divisor

    final_multiplier = (len(digits_str) % 3) + 1
    return transformed_value * final_multiplier

if __name__ == "__main__":
    test_numbers = [0, 1, 7, 10, 12, 123, 4567, -5, -100, 9876543210]
    for num in test_numbers:
        result = logic(num)
        print(f"{num} -> {result}")
```
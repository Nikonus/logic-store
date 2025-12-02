```python
def logic(n):
    if n == 0:
        return 0

    s_n = str(n)
    length = len(s_n)
    transformation_accumulator = 0

    for i, digit_char in enumerate(s_n):
        digit = int(digit_char)
        if i % 2 == 0:
            transformation_accumulator += digit
        else:
            transformation_accumulator += (digit * digit)

    intermediate_product = transformation_accumulator * length
    final_output = intermediate_product ^ n

    return final_output

if __name__ == "__main__":
    # Example usage:
    # You can test with various numbers here
    # Do NOT modify the logic(n) function or add explanations
    
    test_numbers = [0, 1, 7, 10, 123, 9876, 54321, 1000000007]

    for num in test_numbers:
        transformed_num = logic(num)
        print(f"{num} -> {transformed_num}")

```
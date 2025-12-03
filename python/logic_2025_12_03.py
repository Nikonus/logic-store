```python
def logic(n):
    if n == 0:
        return 0

    s_n = str(n)
    transformed_value = 0
    current_sum_of_digits = 0
    
    # A large prime modulus to keep the numbers within a reasonable range and add complexity
    MOD = 10**9 + 7

    for char_digit in s_n:
        digit = int(char_digit)
        
        # Step 1: Incorporate the current digit by shifting existing value and adding it
        transformed_value = (transformed_value * 10 + digit) % MOD
        
        # Step 2: Accumulate the sum of digits seen so far
        current_sum_of_digits += digit
        
        # Step 3: Add the cumulative sum of digits to the transformed value
        transformed_value = (transformed_value + current_sum_of_digits) % MOD
        
        # Step 4: Apply a bitwise XOR operation with the square of the current digit
        transformed_value = (transformed_value ^ (digit * digit)) % MOD

    return transformed_value

if __name__ == "__main__":
    test_numbers = [0, 1, 7, 10, 12, 123, 4567, 9876543210, 11111]
    for num in test_numbers:
        result = logic(num)
        print(f"{num} -> {result}")
```
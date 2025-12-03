```python
import math

def logic(n):
    sign = 1 if n >= 0 else -1
    n_abs = abs(n)
    s_n = str(n_abs)
    num_digits = len(s_n)

    total_weighted_sum = 0
    product_non_zero_digits = 1
    alternating_digit_sum = 0

    for i, char_digit in enumerate(s_n):
        digit = int(char_digit)
        total_weighted_sum += digit * (i + 1)

        if digit != 0:
            product_non_zero_digits *= digit
        
        if i % 2 == 0:
            alternating_digit_sum += digit
        else:
            alternating_digit_sum -= digit

    intermediate_a = (n_abs + total_weighted_sum) * num_digits
    
    multiplier_b = (product_non_zero_digits + alternating_digit_sum) % 10 + 1 
    
    transformed_val_abs = intermediate_a * multiplier_b

    sqrt_n_abs = int(math.isqrt(n_abs))
    if sqrt_n_abs * sqrt_n_abs == n_abs:
        transformed_val_abs += sqrt_n_abs
    else:
        transformed_val_abs -= num_digits

    return transformed_val_abs * sign

if __name__ == "__main__":
    test_numbers = [0, 1, 5, 10, 17, 25, 123, -42, 98765, -100, 1024, 123456789, -12345]
    for num in test_numbers:
        result = logic(num)
        print(f"logic({num}) = {result}")
```
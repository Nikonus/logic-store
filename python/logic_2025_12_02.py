```python
import math

def logic(n):
    if n < 0:
        return logic(abs(n)) * -1

    if n == 0:
        return 0

    binary_representation = bin(n)[2:]
    
    reversed_binary = binary_representation[::-1]
    
    decimal_from_reversed_binary = int(reversed_binary, 2)
    
    sum_of_digits = 0
    temp_n = n
    while temp_n > 0:
        sum_of_digits += temp_n % 10
        temp_n //= 10
        
    final_transformation = decimal_from_reversed_binary + sum_of_digits
    
    return final_transformation

if __name__ == "__main__":
    print(logic(0))
    print(logic(1))
    print(logic(6))
    print(logic(13))
    print(logic(100))
    print(logic(7))
    print(logic(31))
    print(logic(-5))
    print(logic(12345))
```
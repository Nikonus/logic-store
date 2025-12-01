```python
def _get_prime_factors(num):
    factors = []
    d = 2
    temp = num
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

def logic(n):
    if n < 0:
        return -logic(abs(n))
    if n == 0:
        return 0
    if n == 1:
        return 1

    factors = _get_prime_factors(n)
    sum_of_factors = sum(factors)
    
    return n ** sum_of_factors

def main():
    test_numbers = [
        -10, -5, -2, -1, 0, 1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 12, 13, 15, 17, 20, 
        25, 30, 42, 100, 121, 200, 1000
    ]
    for num in test_numbers:
        transformed_value = logic(num)
        print(f"{num} -> {transformed_value}")

if __name__ == "__main__":
    main()
```
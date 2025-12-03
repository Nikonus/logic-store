#!/usr/bin/env python3

def logic(n):
    def _to_base_n(num, base):
        if num == 0:
            return "0"
        digits = []
        while num > 0:
            digits.append(str(num % base))
            num //= base
        return "".join(digits[::-1])

    def _from_base_n(s, base):
        res = 0
        power = 0
        for digit_char in s[::-1]:
            res += int(digit_char) * (base ** power)
            power += 1
        return res

    transformation_base = 7

    n_in_base = _to_base_n(n, transformation_base)
    
    if len(n_in_base) > 1:
        shifted_n_in_base = n_in_base[1:] + n_in_base[0]
    else:
        shifted_n_in_base = n_in_base
    
    transformed_val_base10 = _from_base_n(shifted_n_in_base, transformation_base)

    original_n_str = str(n)
    sum_of_digits_original = sum(int(digit) for digit in original_n_str)

    return (n ^ transformed_val_base10) + sum_of_digits_original

if __name__ == "__main__":
    print(f"logic(0) = {logic(0)}")
    print(f"logic(1) = {logic(1)}")
    print(f"logic(5) = {logic(5)}")
    print(f"logic(7) = {logic(7)}")
    print(f"logic(42) = {logic(42)}")
    print(f"logic(123) = {logic(123)}")
    print(f"logic(1000) = {logic(1000)}")
    print(f"logic(987654321) = {logic(987654321)}")
```cpp
#include <iostream>

long long logic(long long n) {
    if (n == 0) return 0;

    long long original_n_abs = n;
    bool is_negative = false;
    if (n < 0) {
        is_negative = true;
        original_n_abs = -n;
    }

    long long sum_digits = 0;
    long long product_digits = 1;
    long long num_digits = 0;
    long long temp_n_for_stats = original_n_abs;

    while (temp_n_for_stats > 0) {
        long long digit = temp_n_for_stats % 10;
        sum_digits += digit;
        product_digits *= digit;
        num_digits++;
        temp_n_for_stats /= 10;
    }

    long long unique_composite_value = 0;
    long long current_digit_position_weight = 1;
    long long temp_n_for_composite = original_n_abs;
    const long long MODULUS_PRIME = 1000000007; // A large prime for intermediate results

    while(temp_n_for_composite > 0) {
        long long digit = temp_n_for_composite % 10;
        
        // Combine digit, position, and sum/count properties
        long long term = (digit * current_digit_position_weight);
        term ^= (sum_digits + num_digits);
        term %= MODULUS_PRIME;
        
        unique_composite_value = (unique_composite_value + term) % MODULUS_PRIME;
        
        current_digit_position_weight = (current_digit_position_weight * 17) % MODULUS_PRIME; // Arbitrary multiplier
        if (current_digit_position_weight == 0) current_digit_position_weight = 1; // Prevent zero if modulo makes it so

        temp_n_for_composite /= 10;
    }

    long long result = (sum_digits + product_digits);
    result ^= unique_composite_value;
    result *= (num_digits + 1);
    result += (original_n_abs % 19); 

    if (is_negative) {
        result = -result;
    }

    return result;
}

int main() {
    std::cout << "Enter a number: ";
    long long input_n;
    std::cin >> input_n;

    long long transformed_n = logic(input_n);

    std::cout << "Original: " << input_n << std::endl;
    std::cout << "Transformed: " << transformed_n << std::endl;

    std::cout << "\nTesting with other values:" << std::endl;
    std::cout << "logic(0) = " << logic(0) << std::endl;
    std::cout << "logic(1) = " << logic(1) << std::endl;
    std::cout << "logic(123) = " << logic(123) << std::endl;
    std::cout << "logic(987654321) = " << logic(987654321) << std::endl;
    std::cout << "logic(-123) = " << logic(-123) << std::endl;
    std::cout << "logic(1000) = " << logic(1000) << std::endl;
    std::cout << "logic(1234567890) = " << logic(1234567890) << std::endl;
    std::cout << "logic(54321) = " << logic(54321) << std::endl;

    return 0;
}
```
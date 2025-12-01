```cpp
#include <iostream>
#include <cmath>   // For std::sqrt
#include <cstdlib> // For std::llabs (long long absolute value)

long long logic(long long n) {
    long long original_n = n;
    long long abs_n = std::llabs(n);

    long long transformed_val = 0;
    long long temp_n = abs_n;

    if (temp_n == 0) {
        return 0;
    }

    while (temp_n > 0) {
        int digit = temp_n % 10;
        if (digit % 2 == 0) {
            transformed_val += static_cast<long long>(digit) * digit;
        } else {
            transformed_val += static_cast<long long>(digit) * digit * digit;
        }
        temp_n /= 10;
    }

    long long root = static_cast<long long>(std::sqrt(static_cast<double>(abs_n)));
    bool is_perfect_square = (root * root == abs_n);

    long long final_result;
    if (is_perfect_square) {
        final_result = transformed_val ^ abs_n;
    } else {
        final_result = transformed_val + abs_n;
    }

    if (original_n < 0 && final_result != 0) {
        return -final_result;
    }
    return final_result;
}

int main() {
    long long input_n;
    std::cin >> input_n;
    long long output = logic(input_n);
    std::cout << output << std::endl;
    return 0;
}
```
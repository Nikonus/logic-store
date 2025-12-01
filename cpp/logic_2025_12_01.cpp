```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cmath> // For std::abs

long long logic(long long n) {
    if (n == 0) {
        return 0;
    }

    bool is_negative = n < 0;
    long long abs_n = std::abs(n);

    std::string s = std::to_string(abs_n);
    std::string transformed_s = "";
    int position = 0; // 0-indexed position from left (most significant digit)

    for (char digit_char : s) {
        int digit = digit_char - '0';
        // Transformation: each digit is shifted by (its position modulo 3), then the result is taken modulo 10.
        int transformed_digit = (digit + (position % 3)) % 10;
        transformed_s += std::to_string(transformed_digit);
        position++;
    }

    long long transformed_val = std::stoll(transformed_s);

    return is_negative ? -transformed_val : transformed_val;
}

int main() {
    std::vector<long long> test_cases = {
        0,
        1,
        9,
        10,
        123,
        4567,
        98765,
        -1,
        -10,
        -543,
        -999999999999999999LL,
        123456789012345LL
    };

    for (long long val : test_cases) {
        std::cout << val << " -> " << logic(val) << std::endl;
    }

    return 0;
}
```
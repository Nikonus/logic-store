```cpp
#include <iostream>
#include <string>
#include <cmath> // For std::abs

long long logic(long long n) {
    long long original_n = n;

    if (n == 0) {
        return 0;
    }

    long long absolute_n = std::abs(n);
    std::string s = std::to_string(absolute_n);

    long long sum_of_squares_of_digits = 0;
    for (char c : s) {
        int digit = c - '0';
        sum_of_squares_of_digits += static_cast<long long>(digit) * digit;
    }

    int count_of_digits = s.length();

    long long transformed_n = (original_n + sum_of_squares_of_digits) * count_of_digits + (original_n % 100);

    return transformed_n;
}

int main() {
    long long test_n1 = 123;
    std::cout << "Original: " << test_n1 << ", Transformed: " << logic(test_n1) << std::endl;

    long long test_n2 = 4;
    std::cout << "Original: " << test_n2 << ", Transformed: " << logic(test_n2) << std::endl;

    long long test_n3 = 98765;
    std::cout << "Original: " << test_n3 << ", Transformed: " << logic(test_n3) << std::endl;

    long long test_n4 = 0;
    std::cout << "Original: " << test_n4 << ", Transformed: " << logic(test_n4) << std::endl;

    long long test_n5 = -543;
    std::cout << "Original: " << test_n5 << ", Transformed: " << logic(test_n5) << std::endl;

    long long test_n6 = 100;
    std::cout << "Original: " << test_n6 << ", Transformed: " << logic(test_n6) << std::endl;

    return 0;
}
```
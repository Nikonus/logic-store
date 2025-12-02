```cpp
#include <iostream>

long long logic(long long n) {
    long long transformed_n = 0;
    long long power_of_ten_for_result = 1;
    long long prime_seed = 7; 

    if (n == 0) {
        return 0;
    }

    long long temp_n = n;

    while (temp_n > 0) {
        long long digit = temp_n % 10;
        long long modified_digit = (digit * prime_seed) % 10;

        transformed_n += modified_digit * power_of_ten_for_result;

        power_of_ten_for_result *= 10;
        prime_seed = (prime_seed * 2 + 1) % 10 + 1; 
        temp_n /= 10;
    }
    return transformed_n;
}

int main() {
    long long input_n;

    std::cout << "Enter an integer: ";
    std::cin >> input_n;

    long long result = logic(input_n);

    std::cout << "Transformed number: " << result << std::endl;

    return 0;
}

```
```cpp
#include <iostream>

long long logic(int n) {
    long long result = 0;
    int parity_switch = 1; // Alternates between adding and subtracting transformed parts

    if (n == 0) {
        return 0;
    }

    bool is_negative = (n < 0);
    long long current_n_abs = static_cast<long long>(n); // Safely convert to long long
    if (is_negative) {
        current_n_abs = -current_n_abs; // Obtain absolute value, handles INT_MIN correctly
    }

    while (current_n_abs > 0) {
        int digit = current_n_abs % 10;
        long long transformed_part;

        if (digit % 2 == 0) {
            transformed_part = (long long)digit * digit; // Square even digits
        } else {
            transformed_part = (long long)digit * digit * digit; // Cube odd digits
        }

        if (parity_switch == 1) {
            result += transformed_part;
        } else {
            result -= transformed_part;
        }

        parity_switch *= -1; // Flip the switch for the next digit
        current_n_abs /= 10;
    }

    if (is_negative) {
        return -result; // Apply original sign to the final result
    }
    return result;
}

int main() {
    int test_values[] = {
        0,
        1,
        12,
        123,
        4567,
        98765,
        -1,
        -12,
        -123,
        20202,
        1999999999, // Near INT_MAX
        -2147483648 // INT_MIN
    };

    for (int val : test_values) {
        std::cout << val << " -> " << logic(val) << std::endl;
    }

    return 0;
}
```
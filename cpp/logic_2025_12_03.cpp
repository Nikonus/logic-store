```cpp
#include <iostream>

long long logic(long long n) {
    if (n == 0) return 0;

    long long original_n = n;
    long long transformed_val = 0;
    long long multiplier = 1;
    long long bit_manip_factor = 0;
    const long long MOD = 999999937; // A large prime number

    while (n > 0) {
        long long digit = n % 10;
        
        long long transformed_digit_part = (digit * 7 + 13) % 19; 
        
        transformed_val = (transformed_val + (transformed_digit_part * multiplier)) % MOD;
        
        multiplier = (multiplier * 10) % MOD; 
        
        bit_manip_factor ^= (1LL << digit); 
        
        n /= 10;
    }
    
    return (transformed_val ^ bit_manip_factor ^ original_n) % MOD;
}

int main() {
    std::cout << "logic(0) = " << logic(0) << std::endl;
    std::cout << "logic(1) = " << logic(1) << std::endl;
    std::cout << "logic(7) = " << logic(7) << std::endl;
    std::cout << "logic(10) = " << logic(10) << std::endl;
    std::cout << "logic(123) = " << logic(123) << std::endl;
    std::cout << "logic(4567) = " << logic(4567) << std::endl;
    std::cout << "logic(9876543210LL) = " << logic(9876543210LL) << std::endl;
    std::cout << "logic(123456789012345LL) = " << logic(123456789012345LL) << std::endl;

    return 0;
}
```
```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

long long logic(long long n) {
    if (n == 0) {
        return 0;
    }

    std::string s = std::to_string(n);

    std::string largest_permutation_str = s;
    std::sort(largest_permutation_str.rbegin(), largest_permutation_str.rend());

    std::string smallest_permutation_str = s;
    std::sort(smallest_permutation_str.begin(), smallest_permutation_str.end());

    long long largest_num = std::stoll(largest_permutation_str);
    long long smallest_num = std::stoll(smallest_permutation_str);

    return largest_num - smallest_num;
}

int main() {
    std::cout << "Enter an integer: ";
    long long input_n;
    std::cin >> input_n;

    long long transformed_n = logic(input_n);

    std::cout << "Transformed number: " << transformed_n << std::endl;

    return 0;
}
```
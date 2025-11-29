// Auto logic (2025_11_29) token=57d120f4

#include <bits/stdc++.h>
using namespace std;

int logic(int n) {
    int v = n;
    string t = "57d120f4";
    for (int i = 0; i < t.size(); i++) {
        v = (v * 3 + t[i]) ^ i;
    }
    return v;
}

int main() {
    cout << logic(10);
}

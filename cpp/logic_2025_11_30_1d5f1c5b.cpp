// Auto logic 2025_11_30, token=1d5f1c5b
#include <bits/stdc++.h>
using namespace std;

int logic(int n) {
    int v = n;
    string t = "1d5f1c5b";
    for (int i = 0; i < t.size(); i++) {
        v = (v * 3 + t[i]) ^ i;
    }
    return v;
}

int main() {
    cout << logic(10);
}

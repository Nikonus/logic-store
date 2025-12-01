// Auto logic 2025_12_01, token=1f797d5c
#include <bits/stdc++.h>
using namespace std;

int logic(int n) {
    int v = n;
    string t = "1f797d5c";
    for (int i = 0; i < t.size(); i++) {
        v = (v * 3 + t[i]) ^ i;
    }
    return v;
}

int main() {
    cout << logic(10);
}

// Auto logic 2025_11_30, token=a183dc8e
#include <bits/stdc++.h>
using namespace std;

int logic(int n) {
    int v = n;
    string t = "a183dc8e";
    for (int i = 0; i < t.size(); i++) {
        v = (v * 3 + t[i]) ^ i;
    }
    return v;
}

int main() {
    cout << logic(10);
}

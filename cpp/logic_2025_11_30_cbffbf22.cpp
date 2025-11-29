// Auto logic 2025_11_30, token=cbffbf22
#include <bits/stdc++.h>
using namespace std;

int logic(int n) {
    int v = n;
    string t = "cbffbf22";
    for (int i = 0; i < t.size(); i++) {
        v = (v * 3 + t[i]) ^ i;
    }
    return v;
}

int main() {
    cout << logic(10);
}

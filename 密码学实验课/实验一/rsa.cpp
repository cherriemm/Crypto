#include <bits/stdc++.h>
#define N 10000
using namespace std;

int output_prime() {
    int cnt = 0;
    vector<int> is_prime(N, 1);
    for (int i = 2; i < N; i++) {
        if (!is_prime[i])
            continue;
        for (int j = 2; j * j < i; j++) {
            if (!i % j)
                is_prime[i] = 0;
        }
        if (is_prime[i]) {
            for (int j = 2 * i; j < N; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    for (int i = 2; i < N; i++) {
        if (is_prime[i]) {
            cout << i << " ";
            cnt++;
        }
    }
    return cnt;
}

int main() {
    int cnt = output_prime();
    cout << endl <<  "1-10000范围内的素数共有：" + to_string(cnt);
}
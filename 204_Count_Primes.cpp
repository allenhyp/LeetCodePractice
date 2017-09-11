#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        vector<bool> isPrime(n, true);
        isPrime[0] = false, isPrime[1] = false;
        for (int i = 0; i < sqrt(n); i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return count(isPrime.begin(), isPrime.end(), true);
    }
};

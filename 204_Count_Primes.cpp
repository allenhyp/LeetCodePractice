#include <iostream>
#include <math.h>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        int count = 0;
        if (n > 2) {
            count = 1;
        }
        else {
            return 0;
        }
        int i = 3;        
        while (i < n) {
            if (isPrime(i)) {
                count ++;
            }
            i += 2;
        }
        return count;
    }
    bool isPrime(int d) {
        int squarRoot = sqrt(d);
        for (int i = 2; i <= squarRoot; i++) {
            if (d % i == 0) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution mySolution;
    int input = 0;
    cin >> input;
    cout << "RESULT = " << mySolution.countPrimes(input) << endl;
    return 0;
}

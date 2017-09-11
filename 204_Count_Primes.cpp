#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        int count = 0;
        if (n > 2) 
            count = 1;        
        else
            return 0;
        int i = 3;                
        vector<int> usedPrimes;
        usedPrimes.push_back(2);
        while (i < n) {
            if (isPrime(i, usedPrimes))
                count ++;
            i += 2;
        }
        return count;
    }
    bool isPrime(int d, vector<int>& primes) {
        int squarRoot = sqrt(d);
        for (vector<int>::iterator it = primes.begin(); *it <= squarRoot && it != primes.end(); ++it) {
            if (d % *it == 0)
                return false;
        }
        primes.push_back(d);
        return true;
    }
};

int main() {
    Solution mySolution;
    int input = 0;
    cout << "INPUT: ";
    cin >> input;
    cout << "RESULT = " << mySolution.countPrimes(input) << endl;
    return 0;
}

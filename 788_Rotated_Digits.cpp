#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int rotatedDigits(int N) {
        int *nums = new int [N+1];
        int result = 0;
        for (int i = 1; i <= N; i++)
            nums[i] = 0;
        if (N >= 2) nums[2] = 1;
        else return 0;
        if (N >= 5) nums[5] = 1;
        else return 1;
        if (N >= 6) nums[6] = 1;
        else return 2;
        if (N >= 9) nums[9] = 1;
        else return 3;
        result = 4;
        nums[0] = 2;
        nums[1] = 2;
        nums[8] = 2;
        int head = 1, digits = 10;
        for (int i = 10; i <= N; i++) {
            if (i >= digits * 10)
                digits *= 10;
            head = i / digits;
            if (head == 2 || head == 5 || head == 6 || head == 9) {
                if (nums[i - head * digits] > 0) {
                    result++;
                    nums[i] = 1;
                }
            }
            else if (head == 0 || head == 1 || head == 8) {
                if (nums[i - head * digits] == 1) {
                    result++;
                    nums[i] = 1;
                }
                else if (nums[i - head * digits] == 2) {
                    nums[i] = 2;
                }
            }
        }
        return result;
    }
};

int main (int argc, char **argv) {
    Solution mySolution = Solution();
    cout << mySolution.rotatedDigits(atoi(argv[1])) << endl;
    return 0;
}

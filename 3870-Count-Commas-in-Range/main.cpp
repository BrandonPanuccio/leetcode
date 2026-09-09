#include <iostream>

class Solution {
public:
    int countCommas(int n) {
        return n < 1000 ? 0 : n - 999;
    }
};

int main() {
    Solution solution = Solution();
    int result = solution.countCommas(1002);
    std::cout << result << std::endl;
}
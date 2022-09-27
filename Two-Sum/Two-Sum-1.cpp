#include <vector>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    vector<int> solution;

    for (int i = 0; i < nums.size(); i++) {
      int currentNumber = nums[i];

      for (int k = i + 1; k < nums.size(); k++) {
        if (currentNumber + nums[k] == target) {
          solution.push_back(i);
          solution.push_back(k);

          return solution;
        }
      }
    }

    return solution;
  }
};

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hashMap;
    vector<int> solution;

    for (int i = 0; i < nums.size(); i++) {
      int findNum = target - nums[i];

      if (hashMap.find(findNum) != hashMap.end()) {

        solution.push_back(hashMap[findNum]);
        solution.push_back(i);
        return solution;
      }
      hashMap[nums[i]] = i;
    }

    return solution;
  }
};

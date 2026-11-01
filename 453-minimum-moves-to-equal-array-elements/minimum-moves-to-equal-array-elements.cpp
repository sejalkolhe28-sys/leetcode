class Solution {
public:
    int minMoves(vector<int>& nums) {
        int minimum = *min_element(nums.begin(), nums.end());
        long long sum = 0;

        for (int value : nums) {
            sum += value;
        }

        return static_cast<int>(sum - 1LL * nums.size() * minimum);
    }
};
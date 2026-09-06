class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int a = nums.size();
        int c = 0;
        for (int i = 0; i < a; i++) {
            long long prod = 1; 
            for (int j = i; j < a; j++) {
                prod = prod * nums[j];
                if (prod < k) {
                    c++;
                } else {
                    break;
                }
            }
        }
        return c;
    }
};

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int i = 0;
        while (true){
            if (nums[i] <= 0 && nums.size() > 1){
                return false;
                break;
            }
            int pos = i;
            i = i + nums[i];
            if (i >= nums.size() - 1){
                return true;
                break;
            }
            else{
                int ctr = 0;
                while (nums[i] == 0){
                    i = i - 1;
                    ++ctr;
                }
                if (i == pos){
                    nums[pos] = nums[pos] - ctr;
                    i = 0;
                    if (nums[i] == 1){
                        nums.erase(nums.begin());
                    }
                }
                else{
                    nums[pos] = nums[pos] - ctr;
                }
            }
        }
    }
};
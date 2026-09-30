#type: ignore 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        return sum([[x[:i] + [nums[-1]] + x[i:] for i in range(len(x) + 1)] for x in self.permute(nums[:-1])], [])
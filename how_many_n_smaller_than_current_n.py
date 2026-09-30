#type: ignore
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums: list[int] = sorted(nums)
        table = [[] for _ in range(len(nums))]
        for i in sorted_nums:
            table[sorted_nums.index(i)].append(i)
        
        count = 0
        final = [0 for _ in range(len(nums))]
        for i in range(1, len(table)):
            count += len(table[i - 1])
            for j in table[i]:
                final[nums.index(j)] = count
                nums[nums.index(j)] = -1
        return(final)
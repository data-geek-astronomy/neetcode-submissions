class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        seen={}
        for i ,num in enumerate(nums):
            diff=target-num

            if diff in seen :
                first=seen[diff]
                second=i
                return [first,second] if first<second else [second, first]

            seen[num]=i        
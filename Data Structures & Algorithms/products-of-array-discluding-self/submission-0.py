class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=[]
        
        for i in range(n):
            multiplier =1 
            for j in range(n):
                if j!=i:
                    multiplier=nums[j]*multiplier
            
            x.append(multiplier)
        
        return x 
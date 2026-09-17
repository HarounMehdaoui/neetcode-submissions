class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all, z=1, 0
        for i in nums:
            if i:
                all*=i
            else: z+=1
        if z>1:
            return [0]*len(nums)
        
        res=[0]*len(nums)
        for i, c in enumerate(nums):
            if z: res[i]=0 if c else all
            else: res[i]=all//c
        
        return res
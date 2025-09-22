class Solution:  
    def findMaxSum(self,arr):
        # code here
        
        # def dfs(nums):
        #     n = len(nums)
        #     if n == 0:
        #         return 0 
        #     if n == 1:
        #         return nums[0]
        #     if n == 2:
        #         return max(nums[0], nums[1])
        #     return max(nums[0]+ dfs(nums[2:]), dfs(nums[1:]))
            
        # return dfs(arr)
        
  
        prev1 = arr[0]
        prev2 = max(arr[1], arr[0])
        
        for i in range(2,len(arr)):
            tmp = max(arr[i]+prev1, prev2)
            prev1 = prev2
            prev2 = tmp
            
        return prev2
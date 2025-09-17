
'''this is to check for tow numbers are ame or not'''
class Solution(object):
    def twoSum(self, nums, target):
        sum =0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    return[i,j]
                

S =Solution()
t= S.twoSum([3,2,4],6)
print(t)
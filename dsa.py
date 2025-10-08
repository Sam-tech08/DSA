
'''this is to check for tow numbers are ame or not'''
class Solution(object):
    def twoSum(self, nums, target):
        sum =0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    return[i,j]
                
'''Given the integer day denoting the day number, print on the screen which day of the week it is.
 Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
Ensure only the 1st letter of the answer is capitalised. '''


class Find_day:
    def Whichweek(self,day):
        if day == 1:
            return "Monday"
        elif day == 2:
            return "Tuesday"
        elif day == 3:
            return "Wednesday"
        elif day == 4:
            return "Thursday"
        elif day == 5:
            return "Friday"
        elif day == 6:
            return "Saturday"
        elif day == 7:
            return "Sunday"
        else:
            return "Invalid"
d = Find_day()
day = d.Whichweek(5)
print(day)


class Sort_Solution:
    def selectionsort(self,nums):
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                for j in range(i+1,len(nums)):
                    if nums[i] > nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
                        
        return nums
    
        
    
s = Sort_Solution()
nums = [7,4,1,5,3]
print(s.selectionsort(nums))
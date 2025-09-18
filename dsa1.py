class Solution(object):
    def isPalindrome(self, x):
        palindrome_value=str(x)
        print(palindrome_value)
        reverse = palindrome_value[::-1]
        print(reverse)
        if palindrome_value == reverse:
            return True
        else:
            return False

s=Solution()
print(s.isPalindrome(-121))

# mergig of 2 list 
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        sum_list=[]
        for i in range(len(list1)):
            sum_list.append(list1[i])
        for i in range(len(list2)):
            sum_list.append(list2[i])
        sum_list.sort()
        
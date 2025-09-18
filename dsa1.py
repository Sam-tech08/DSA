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

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail= tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next


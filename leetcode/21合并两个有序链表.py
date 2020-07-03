# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        ls = []
        for i1 in l1:
            ls.append(i1)
        for i2 in l2:
            ls.append(i2)
        print(ls)

        ls.sort()
        return ls

r = Solution().mergeTwoLists([1,2,3], [1,3,4])
print(r)
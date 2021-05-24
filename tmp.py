

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# # 快慢指针法
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         slow = fast = head
#
#         while fast and fast.next:  ##保证fast和fast.next有值 不然fast.next.next会报错
#             slow = slow.next
#             fast = fast.next.next
#             if slow is fast:
#                 return True
#         return False
#
#
# if __name__ == '__main__':
#     ln1 = ListNode(1)
#     ln2 = ListNode(2)
#     ln1.next = ln2
#     ln2.next = ln1
#     r = Solution().hasCycle(ln1)
#     print(r)

def dp(n):
    if n <= 2:
        return n
    if n > 2:
        return dp(n - 1) + dp(n - 2)

print(dp(4))
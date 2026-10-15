# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def swapNodes(self, head: ListNode | None, k: int) -> ListNode | None:
    p = None  
    q = None 

    curr = head
    while curr:
      if q:
        q = q.next
      k -= 1
      if k == 0:
        p = curr
        q = head
      curr = curr.next

    p.val, q.val = q.val, p.val
    return head
        
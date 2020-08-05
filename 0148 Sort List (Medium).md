# 148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
```
Input: 4->2->1->3
Output: 1->2->3->4
```

Example 2:
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

## Python
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(h1, h2):
            prev_head = node = ListNode(None)
            
            cur_1, cur_2 = h1, h2
            while cur_1 and cur_2:
                if cur_1.val <= cur_2.val:
                    node.next = cur_1
                    cur_1 = cur_1.next
                else:
                    node.next = cur_2
                    cur_2 = cur_2.next
                node = node.next
                node.next = cur_1 or cur_2
            return prev_head.next
                
        def get_mid(head):
            slow = fast = head
            while fast and fast.next:
                prev, slow, fast = slow, slow.next, fast.next.next
            return prev, slow
        
        def sort(head):
            if not head or not head.next:
                return head
            prev_mid, mid = get_mid(head)
            prev_mid.next = None
            h1 = sort(head)
            h2 = sort(mid)
            return merge(h1, h2)
        
        return sort(head)
```

## Java
``` java

```
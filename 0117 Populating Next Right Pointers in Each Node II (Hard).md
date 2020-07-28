# 117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:

![](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)
```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
```

## Python
``` python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root
        
        while True:
            cur = None
            while not cur and leftmost:
                cur = leftmost.left
                if not cur: cur = leftmost.right
                if not cur: leftmost = leftmost.next
            
            if not cur:
                break
            
            head, leftmost = leftmost, cur
            
            while head:
                if head.left and cur != head.left:
                    cur.next = head.left
                    cur = cur.next
                if head.right and cur != head.right:
                    cur.next = head.right
                    cur = cur.next
                head = head.next
                
        return root
            
```

## Java
``` java

```
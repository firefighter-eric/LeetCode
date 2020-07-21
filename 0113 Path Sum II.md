# 113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:
```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
```
Return:
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```
## Python
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def helper(ans, node, s, path):
            if not node:
                return
            
            s += node.val
            path.append(node.val)
            
            if not node.left and not node.right and s == sum:
                ans.append(path.copy())
            else:
                helper(ans, node.left, s, path)
                helper(ans, node.right, s, path)
            
            path.pop()
            return
        
        ans = []
        helper(ans, root, 0, [])
        return ans
```

## Java
``` java

```
# 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```
## Python
``` python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, l, r):
            if l == r == n:
                ans.append(s)
                return
            if l < n:
                backtrack(s + '(', l + 1, r)
            if r < l:
                backtrack(s + ')', l, r + 1)
                
        ans = []
        backtrack('', 0, 0)
        return ans
```

<!-- ## Java
``` java

``` -->
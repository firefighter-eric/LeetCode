# 5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

Example 2:
```
Input: "cbbd"
Output: "bb"
```

## Python
``` python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_pal(l, r) -> str:
            while -1 < l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        
        ans = ''
        for i in range(len(s)):
            s1 = is_pal(i, i)
            s2 = is_pal(i, i + 1)
            ans = max(ans, s1, s2, key = lambda x: len(x))
        return ans
```
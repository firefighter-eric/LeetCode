# 17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

## Python
``` python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        int2char = {'1': (),
                    '2': ('a', 'b', 'c'),
                    '3': ('d', 'e', 'f'), 
                    '4': ('g', 'h', 'i'),
                    '5': ('j', 'k', 'l'),
                    '6': ('m', 'n', 'o'),
                    '7': ('p', 'q' ,'r' ,'s'),
                    '8': ('t', 'u', 'v'),
                    '9': ('w', 'x', 'y' ,'z')}
        
        def backtrack(s, i):
            if i == len(digits):
                ans.append(s)
                return
            for c in int2char[digits[i]]:
                backtrack(s + c, i + 1)
        
        ans = []        
        backtrack('', 0)
        return ans
```

<!-- ## Java
``` java

``` -->
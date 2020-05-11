# 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:
```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

Example 2:
```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Python
``` python

```

## Java
``` java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int max_length = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (int i = 0, start = 0; i < n; i++){
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                start = Math.max(start, map.get(c));
            }
            max_length = Math.max(max_length, i - start + 1);
            map.put(c, i + 1);
        }
        return max_length;
    }
}
```
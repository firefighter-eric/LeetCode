# 39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

## Python
``` python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(res, res_sum, start):
            if res_sum == target:
                ans_set.append(res)
            
            for i in range(start, len(candidates)):
                c = candidates[i]
                if  res_sum + c <= target:
                    backtrack(res + [c], res_sum + c, i)
                    
        ans_set = []
        backtrack([], 0, 0)
        return ans_set
```

## Java
``` java

```
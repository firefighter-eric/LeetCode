# 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

<!-- ## Python
``` python

``` -->

## Java
``` java
class Solution {
    List<List<Integer>> ans;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        ans = new ArrayList();
        Arrays.sort(candidates);
        backtrack(new ArrayList(), 0, candidates, target);
        return ans;
}
    
    private void backtrack(List<Integer> res, int i, int[] candidates, int target) {
        if (target == 0) {
            ans.add(new ArrayList(res));
            return;
        }
        for (; i < candidates.length; i++) {
            int c = candidates[i];
            if (c <= target) {
                res.add(c);
                backtrack(res, i + 1, candidates, target - c);
                res.remove(res.size() - 1);
                while (i + 1 < candidates.length && candidates[i] == candidates[i + 1]) {
                    i++;
                }
            }
        }
        return;
    }
}
```
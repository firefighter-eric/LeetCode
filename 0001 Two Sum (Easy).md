# 1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Python
``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            d[n] = i
```

## Java
``` java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        HashMap<Integer, Integer> m  = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (m.containsKey(target - nums[i])) {
                ans[0] = m.get(target - nums[i]);
                ans[1] = i;
                break;
            }
            m.put(nums[i], i);
        }
        return ans;
    }
}
```
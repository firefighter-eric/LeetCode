# 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

<!-- ## Python
``` python

``` -->

## Java
``` java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int index = binarySearch(nums, target);
        if (index == -1) return new int[] {-1, -1};
        return getRange(nums, index);
    }
    
    private int binarySearch(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return -1;
    }
    
    private int[] getRange(int[] nums, int index) {
        int target = nums[index];
        int l = index;
        int r = index;
        while (l - 1 >= 0 && nums[l - 1] == target) {
            l--;
        }
        while (r + 1 < nums.length && nums[r + 1] == target) {
            r++;
        }
        return new int[] {l, r};
    }
}
```
# 152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
Example 2
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
## Python
``` python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = max_prod
        
        for num in nums[1:]:
            _max = max_prod * num
            _min = min_prod * num
            max_prod, min_prod = max(num, _max, _min), min(num, _max, _min)
            
            result = max(max_prod, result)
            
        return result
```

## Java
``` java

```
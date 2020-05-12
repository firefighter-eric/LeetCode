# 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

## Python
``` python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_func(ind):
            for i in range(0, (len(nums) - ind) // 2):
                nums[ind + i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[ind + i]
        
        i = len(nums) - 2
        while i > -1 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i > -1:
            i_min, j = i + 1, i + 1
            while j < len(nums) and nums[j] > nums[i]:
                i_min = j if (nums[j] <= nums[i_min]) else i_min
                j += 1     
            nums[i], nums[i_min] = nums[i_min], nums[i]
            
        reverse_func(i + 1)
```

<!-- ## Java
``` java

``` -->
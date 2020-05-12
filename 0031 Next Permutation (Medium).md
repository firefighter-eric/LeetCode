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
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1   
            nums[i], nums[j] = nums[j], nums[i]
            
        reverse_func(i + 1)
```

## Java
``` java
class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        while (i > -1 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i > -1) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    private void reverse(int[] nums, int start) {
        int end = nums.length - 1;
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
}
```
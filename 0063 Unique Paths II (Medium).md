# 63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

## Python
``` python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        Y, X = len(obstacleGrid), len(obstacleGrid[0])
        
        obstacleGrid[0][0] = 1
        for x in range(1, X):
            obstacleGrid[0][x] = int(obstacleGrid[0][x - 1] == 1 and obstacleGrid[0][x] == 0)
        for y in range(1, Y):
            obstacleGrid[y][0] = int(obstacleGrid[y - 1][0] == 1 and obstacleGrid[y][0] == 0)

        for y in range(1, Y):
            for x in range(1, X):
                if obstacleGrid[y][x] == 0:
                    obstacleGrid[y][x] = obstacleGrid[y][x - 1] + obstacleGrid[y - 1][x]
                else:
                    obstacleGrid[y][x] = 0

        return obstacleGrid[-1][-1]
```

## Java
``` java

```
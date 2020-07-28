# 123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

Example 2:
```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

Example 3:
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Python
### Solution 1
``` python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost_1, cost_2 = float('inf'), float('inf')
        profit_1, profit_2 = 0, 0
        
        for price in prices:
            cost_1 = min(cost_1, price)
            profit_1 = max(profit_1, price - cost_1)
            cost_2 = min(cost_2, price - profit_1)
            profit_2 = max(profit_2, price - cost_2)
        
        return profit_2
```

### Solution 2
``` python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        L = len(prices)
        profit_l, profit_r = [0] * L, [0] * (L + 1)
        min_l, max_r = prices[0], prices[-1]
        for i in range(1, L):
            profit_l[i] = max(profit_l[i - 1], prices[i] - min_l) 
            min_l = min(min_l, prices[i])
            
            j = L - 1 - i
            profit_r[j] = max(profit_r[j + 1], max_r - prices[j])
            max_r = max(max_r, prices[j])
        
        max_profit = 0
        for i in range(L):
            max_profit = max(max_profit, profit_l[i] + profit_r[i + 1])
        
        return max_profit
```
## Java
``` java

```
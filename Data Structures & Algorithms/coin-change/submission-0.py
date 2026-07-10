class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        coins.sort()

        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount+1):
            local_res = dp[i]
            for coin in coins:
                if i - coin < 0:
                    break
                local_res = min(local_res, 1 + dp[i - coin])
            dp[i] = local_res
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
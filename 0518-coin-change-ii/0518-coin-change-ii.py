class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        counter = 0

        dp=[0 for i in range(amount+1)]
        dp[0]=1

        for coin in coins:
            for current_amount in range(coin, amount+1):
                dp[current_amount]=dp[current_amount] + dp[current_amount-coin]
        return dp[-1]
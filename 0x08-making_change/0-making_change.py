#!usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """Make Change"""
    if total <= 0:
        return 0
    dp = [total + 1 for x in range(total + 1)]
    dp[0] = 0
    for c in coins:
        for x in range(c, total + 1):
            dp[x] = min(dp[x], dp[x - c] + 1)
    if dp[total] != total + 1:
        return dp[total]
    else:
        return -1

#!/usr/bin/python

def rep_134(n):
    dp = [None] * 4
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    if n <= 0:
        return 0

    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-3] + dp[i-4])
    
    return dp[n]

def main():
    print rep_134(3)

if __name__ == "__main__":
    main()
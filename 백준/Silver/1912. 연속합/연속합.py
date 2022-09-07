def solution():
    n = input("")
    numArr = input("")
    n = int(n)
    numArr = numArr.split(" ")
    numArr = list(map(int, numArr))

    dp = [0] * n
    dp[0] = numArr[0]

    for i in range(1, len(numArr)):
        if dp[i-1] >= 0:
            dp[i] = dp[i - 1] + numArr[i]
        else:
            dp[i] = numArr[i]
    print(max(dp))
    return 0
solution()
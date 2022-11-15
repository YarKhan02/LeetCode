def majority():
    nums = [2,2,1,1,1,2,2]

    memo = {}
    output = 0 

    for i, n in enumerate(nums):
        if n not in memo:
            memo[n] = 0
        if n in memo:
            memo[n] = memo[n] + 1
            output = max(output, memo[n])

    key = [k for k, v in memo.items() if v == output]

    return key
        

print(majority())

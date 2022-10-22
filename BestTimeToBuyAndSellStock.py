def best_time_to_buy_and_sell_stock(nums):
    n = len(nums)
    buy = 0
    sell = 1

    while True:
        if buy == n or sell == n:
            return max_profit

        if nums[sell] > nums[buy]:
            profit = nums[sell] - nums[buy]
            max_profit = max(max_profit, profit)
            sell += 1

        elif nums[sell] < nums[buy]:
            buy += 1
            sell = buy + 1

        else:
           buy += 1 
           sell = buy + 1

print(best_time_to_buy_and_sell_stock([1,2,4,2,5,7,2,4,9,0,9]))





def best_time_to_buy_and_sell_stock(nums):
    maxP = 0
    maximum = 0

    for i in range(1, len(nums)):
        maxP = max(maxP + (nums[i] - nums[i - 1]), 0)
        maximum = max(maximum, maxP)

    return maximum

print(best_time_to_buy_and_sell_stock([1,2,4,2,5,7,2,4,9,0,9]))
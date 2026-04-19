def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

prices = [635, 864, 247, 325, 257, 745, 245]
print("Maximum Profit:", max_profit(prices))

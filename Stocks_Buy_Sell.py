prices = [635, 864, 247, 325, 257, 745, 245]

def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit

print("Maximum Profit:", max_profit(prices))

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

stock_qn = int(input("What analysis do you want to perform? : \n 1. Find the highest stock price \n 2. Find the lowest stock price \n 3. Find the stock price on a specific day \nEnter:"))

if stock_qn == 1:
    def highest_stock_price(prices):
        max_price = prices[0]
        for price in prices:
            if price > max_price:
                max_price = price
        return max_price

    print("Highest stock price:", highest_stock_price(stock_prices))
elif stock_qn == 2:
    def lowest_stock_price(prices):
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
        return min_price
    print("Lowest stock price:", lowest_stock_price(stock_prices))
elif stock_qn == 3:
    day = int(input("Enter the day number (1-20): "))
    def price_at(prices, day):
        if day < 1 or day > len(prices):
            return "Invalid day number"
        return prices[day - 1]
    print(f"Stock price on day {day}:", price_at(stock_prices, day))
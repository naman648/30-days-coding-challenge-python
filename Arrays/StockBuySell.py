def StockBuySell(arr):
        n = len(arr)
        max_profit = 0
        max_price = 0
        min_price = 0
        for i in range(n):
            for j in range(i+1,n):
                profit = arr[j] - arr[i]
                if profit > max_profit:
                    max_profit = profit
                    max_price = j
                    min_price = i                  
        return max_profit, max_price, min_price

arr = [5,1,4,7,3,6]
result = StockBuySell(arr)
print(result)
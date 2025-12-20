# Stock market analysis
stocks = {
    "ABC": [100, 110, 105, 120],
    "XYZ": [200, 195, 210, 220]
}

for stock, prices in stocks.items():
    change = prices[-1] - prices[0]
    print(stock, "Net Change:", change)

# Dictionary
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 420
}

total_investment = 0

print("Stock Portfolio Tracker")


# Asking user how many different stocks they want to enter
n = int(input("How many stocks do you want to enter: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if stock in stocks:
        value = stocks[stock] * qty
        total_investment += value
        print(stock, "Value:", value)
    else:
        print("Stock not found")

print("Total Investment:", total_investment)

save = input("Save result to file? yes/no: ").lower()
# If user chooses yes then save data in a text file
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio\n")
        f.write("Total Investment: " + str(total_investment))
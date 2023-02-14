dailyLemonadeSales = [[5, 7, 2], [5, 7, 2, 4], [8, 9], [2, 7, 2, 1, 9], [7, 4, 6]]
pricePerCup = 0.75
costPerCup = 0.20
totalSales = 0
totalProfit = 0.0



# Complete the nested loop below so that the total number of cups sold is added to totalSales
# Each list inside of dailyLemonadeSales can be considered a day with multiple sales recorded
for day in dailyLemonadeSales:
    for cupsSold in day:
        totalSales += cupsSold
else:
    print(totalSales)

# Complete the following code block to calculate the profit for each day, and add each value to 
# the total profit. Remember to check the variables defined above to calculate profit!
for day in dailyLemonadeSales:
    dailyOperatingCost = 0.0
    dailyTotalIncome = 0.0
    dailyProfit = 0.0
    dailySales = 0.0
    for cupsSold in day:
        dailySales += cupsSold
    dailyOperatingCost = dailySales * costPerCup
    dailyTotalIncome = dailySales * pricePerCup
    dailyProfit = round(dailyTotalIncome - dailyOperatingCost, 2)
    totalProfit += dailyProfit
    print(dailyProfit)
print(totalProfit)

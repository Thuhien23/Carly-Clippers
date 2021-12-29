# sum up all the prices of haircuts
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# Loop through the prices list and add each price to the variable total_price
total_price = 0
for i in prices:
  total_price += i
print(total_price)
# calculate average price
average_price = total_price/len(prices)
print("Average Haircut Price: "+ str(average_price))
# Carly wants to cut all prices by 5 dollars.
new_prices = [i - 5 for i in prices]
print(new_prices)
# calculate revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))
# average daily revenue
average_daily_revenue =total_revenue/7
print(average_daily_revenue)
# haircuts under 30
cuts_under_30 =[]
for i in range(len(new_prices)):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
print(cuts_under_30)

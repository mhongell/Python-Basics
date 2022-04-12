### This is another project I did learning the basics of Python. This one is a lot of work with lists

# Create list
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
# Count amount of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# Length of toppings list
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")
# 2D list of topping and price
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
# Sort pizza_and_prices ascending
pizza_and_prices.sort()
print(pizza_and_prices)
# Store first element in list to new variable
cheapest_pizza = pizza_and_prices[:1]
print(cheapest_pizza)
# Store last element in list to new variable
priciest_pizza = pizza_and_prices[-1:]
print(priciest_pizza)
# Remove anchovies slice
pizza_and_prices.pop(-1)
print(pizza_and_prices)
# Add new pizza to list
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
# Slice 3 cheapest zas in new list
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

# Your code below:

toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
print(toppings)

prices = [2, 6, 1, 3, 2 ,7, 2]
print(prices)

num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(num_pizzas)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"],[7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

print("Sorted pizza")
pizza_and_prices.sort()
print(pizza_and_prices)

print("Cheapest Pizza")
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

print("Priciest Pizza:")
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

print("No mo fishies")
pizza_and_prices.remove([7, "anchovies"])
print(pizza_and_prices)

print("Plus peppers")
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

print("Cheapest three:")
three_cheapest = pizza_and_prices[0] + pizza_and_prices[1] + pizza_and_prices[2]
print(three_cheapest)

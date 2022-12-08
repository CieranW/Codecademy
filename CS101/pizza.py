# Your code below:
toppings = ["Pepperoni", "Pineapple", "Cheese",
            "Sausage", "Olives", "Anchovies", "Mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slice = prices.count(2)
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Combine toppings and prices with prices coming first.
pizza_and_prices = zip(prices, toppings)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
# Remove anchovies and add peppers.
pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, "Peppers"])
for price_and_pizza in pizza_and_prices:
    print(price_and_pizza)
# Find the three cheapest pizzas.
three_cheapest = pizza_and_prices[:3]
print("The three cheapest pizzas are: ", three_cheapest)

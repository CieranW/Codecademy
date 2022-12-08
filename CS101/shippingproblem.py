# Script to use given shipping costs to calculate the cheapest option. Weight is inputed by user.
from decimal import Decimal

weight = float(input("Enter your package's weight: "))
print(weight, "kg")

# Ground shipping
if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight <= 6:
    cost_ground = weight * 3.00 + 20
elif weight <= 10:
    cost_ground = weight * 4.00 + 20
else:
    cost_ground = weight * 4.75 + 20
print("Ground cost is $", cost_ground)

# Ground shipping premium
cost_premium = 125.00
print("Premium cost is $", cost_premium)

# Drone shipping
if weight <= 2:
    cost_drone = weight * 4.5
elif weight <= 6:
    cost_drone = weight * 9.0
elif weight <= 10:
    cost_drone = weight * 12.0
else:
    cost_drone = weight * 14.25
print("Drone cost is $", Decimal(cost_drone))

# Comparing costs and evaluating cheapest method of shipping

ground = cost_ground
premium = cost_premium
drone = cost_drone

if (ground < premium) and (ground < drone):
    print("Ground shipping is the cheapest option.")
elif (premium < ground) and (premium < drone):
    print("Premium shipping is the cheapest option.")
elif (drone < ground) and (drone < premium):
    print("Drone shipping is the cheapest option.")

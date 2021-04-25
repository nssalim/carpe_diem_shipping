# Control Flow - Python
# Project 2 - "Seas the day" and ship that package!

# Carpe Diem Shipping takes the weight of a package and determines the cheapest way to ship that package.

# The customer has 3 options:-
# Ground Shipping
# Ground Shipping Premium
# Drone Shipping


# Weight of package (lb)
weight = 41.5
# For a 41.5 pound package, GROUND SHIPPING PREMIUM is the cheapest ($125.0).


# GROUND SHIPPING
# Has a small flat charge ($20) plus a rate based on the weight of the package.
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
# A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping
else:
  cost_ground = weight * 4.75 + 20
print("Ground Shipping $", cost_ground)


# GROUND SHIPPING PREMIUM
# Has a flat charge ($125.00), but no charge for weight.
cost_ground_premium = 125.00
print("Ground Shipping Premimium $", cost_ground_premium)

 
# DRONE SHIPPING
# Has no flat charge, but the rate based on weight is triple the rate of ground shipping.
if weight <= 2:
  cost_drone = weight * 4.50
# A package that weighs 1.5 pounds should cost $6.75 to ship by drone
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25
print("Drone Shipping: $", cost_drone)


# weight = 4.8
# For a 4.8 pound package, GROUND SHIPPING is the cheapest ($34.4).
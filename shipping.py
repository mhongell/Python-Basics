### This is the third project I did in my CodeCademy course. It is more else/if practice for determining the cost for three different shipping methods ###

# Set your weight variable 
weight = 41.5

## Ground Shipping price table ##

#Flat charge of 20 across the board
#Weight of Package	Price per Pound	
#2 lb or less	$1.50
#Over 2 lb but less than or equal to 6 lb	$3.00
#Over 6 lb but less than or equal to 10 lb	$4.00	
#Over 10 lb	$4.75

# If/else statements:
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Ground Shipping $", cost_ground)

## Premium Ground Shipping ##
# This does not change with weight, instead it is one flat charge
cost_ground_premium = 125
print ("Ground Shipping Premium $", cost_ground_premium)

## Drone Shipping ##
# No flat charge, but the rate based on weight is triple the rate of ground shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25
print("Drone Shipping $", cost_drone)

### Answers for a couple packages ###
# 4.8 pound package
#Ground Shipping $ 34.4
#Ground Shipping Premium $ 125
#Drone Shipping $ 43.199999999999996

# 41.5 pound package
#Ground Shipping $ 217.125
#Ground Shipping Premium $ 125
#Drone Shipping $ 591.375

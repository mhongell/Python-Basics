## This was my first project I completed through CodeCademy. It updates variables according to what a customer is shopping for.
## This teaches how integers and strings can be added to existing variables.

### Variables Set ###
# Lovely Loveseat Variables
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

#Stylish Settee Variables
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

# Luxurious Lamp Variables
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

# Sales Tax Variable
sales_tax = .088

# Customer One Variables
customer_one_total = 0
customer_one_itemization = ""

### Customer One Starts Here ###
# Customer One Purchases Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Customer One Purchases Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Customer One Sales Tax
customer_one_tax = customer_one_total * sales_tax

# Customer One Total Cost
customer_one_total += customer_one_tax

## Generate Receipt Here ##
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

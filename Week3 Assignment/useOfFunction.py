"""
  1. Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

  2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
"""

def calculate_discount(price, discount_percent):
  if discount_percent >= 20 :
    return price * discount_percent * 0.01
  else :
    return price
  
priceVal = float(input("Enter base price of product: "))
discountVal = float(input("Enter product's discount percentage: ").replace("%",""))   # Handling entering of "%"" by user

print(f"Your bill is {calculate_discount(priceVal,discountVal)}")
 
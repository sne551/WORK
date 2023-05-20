#!/usr/bin/env python
# coding: utf-8

# In[40]:


import math


# In[41]:


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# In[42]:


# Create product instances
product1 = Product("Product A", 20.0)
product2 = Product("Product B", 40.0)
product3 = Product("Product C", 50.0)


# In[43]:


# Store products in a list
catalog = [product1, product2, product3]


# In[44]:


# Ask for quantity of each product
cart = {}
for product in catalog:
    quantity = int(input(f"Enter the quantity of {product.name}: "))
    cart[product] = quantity


# In[47]:


# Calculate and display the product details
subtotal = 0.0
print("\nProduct Details:")
for product, quantity in cart.items():
    total_amount = product.price * quantity
    subtotal += total_amount
    print(f"{product.name}: Quantity: {quantity} | Total Amount: ${total_amount:.2f}")


# In[48]:


# Apply discounts
discounts = [
    {"name": "Flat $10 discount", "condition": subtotal > 200.0, "amount": 10.0},
    {"name": "5% discount on Total Amount", "condition": quantity > 10, "amount":total_amount * 0.05},
    {"name": "bulk_10_discount", "condition": total_amount > 20, "amount": subtotal * 0.1},
    {"name": "tiered_50_discount", "condition": total_amount > 30, "amount": subtotal * 0.5}
]


# In[49]:


# Find the most beneficial discount
applicable_discounts = [discount for discount in discounts if discount["condition"]]
if applicable_discounts:
    best_discount = max(applicable_discounts, key=lambda d: d["amount"])
    discounted_total = subtotal - best_discount["amount"]
    print(f"\nDiscount Applied: {best_discount['name']} (${best_discount['amount']:.2f})")
else:
    discounted_total = subtotal
    print("\nNo applicable discounts.")

# Display the subtotal and discounted total
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Discounted Total: ${discounted_total:.2f}")


# In[50]:


# Ask if each product should be wrapped as a gift
gift_wrap_cart = {}
gift_wrap_total = 0
for product, quantity in cart.items():
    if quantity > 0:
        wrap_as_gift = input(f"Do you want to wrap {quantity} unit(s) of {product.name} as a gift? (yes/no): ")
        if wrap_as_gift.lower() == "yes":
            gift_wrap_cart[product] = quantity
            gift_wrap_total += quantity


# In[51]:


# Gift wrap fee and shipping fee
gift_wrap_fee_per_unit = 1
units_per_package = 10
shipping_fee_per_package = 5


# In[52]:


# Calculate gift wrap fee
gift_wrap_fee = gift_wrap_total * gift_wrap_fee_per_unit


# In[53]:


# Calculate and display the total
print(f"Total: ${discounted_total:.2f}")


# In[55]:


# Calculate shipping fee
shipping_fee = math.ceil(total_amount / units_per_package) * shipping_fee_per_package


# In[56]:


# Calculate total amount
total_amount = discounted_total + gift_wrap_fee + shipping_fee


# In[57]:


# Display the subtotal, discounted total, and gift wrap fee
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Discounted Total: ${discounted_total:.2f}")
print(f"Gift Wrap Fee: ${gift_wrap_fee:.2f}")


# In[58]:


# Calculate and display the total
print(f"Total: ${discounted_total:.2f}")


# In[ ]:





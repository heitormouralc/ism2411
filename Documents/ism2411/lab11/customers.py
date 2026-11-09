# ==========================================
# REFLECTION QUESTIONS
# ==========================================
# 1. In Exercise 3 you saw the difference between .get() and bracket notation. When in real work would you use each one, and what's your rule of thumb for choosing?
#    - Use .get() when dealing with external data, APIs, or user inputs where a missing key is expected and should gracefully fall back to a default value without crashing the app. Use bracket notation when the key is strictly required for the logic to function and its absence indicates a critical bug that needs to halt execution with a KeyError.
#
# 2. Exercise 8 asked you to build a summary dictionary with a loop. What does this pattern remind you of from Excel, and why might the Python version be more useful for large datasets?
#    - This pattern reminds me of a Pivot Table or SUMIF formula in Excel, used for grouping and aggregating metrics. The Python version is much more powerful for large datasets because it avoids workbook size limits, handles millions of rows instantly without crashing the interface, and automates complex multi-step pipelines seamlessly.
# ==========================================

# EXERCISE 1 · Beginner: One customer
customer = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00
}

print("--- Exercise 1 ---")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2 · Beginner: Update and add
print("\n--- Exercise 2 ---")
customer["phone"] = "555-0199"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# EXERCISE 3 · Beginner: Safe lookup
print("\n--- Exercise 3 ---")
print("Using .get():", customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError caught: 'email' key no longer exists in dictionary.")


# EXERCISE 4 · Beginner: Iterate
print("\n--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")


# EXERCISE 5 · Intermediate: Lookup table
print("\n--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
current_tier = customer["tier"]
discount_rate = tier_discounts.get(current_tier, 0)

purchase_amount = 200
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {current_tier}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")


# EXERCISE 6 · Intermediate: List of dicts
print("\n--- Exercise 6 ---")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "bronze"}
]

test_purchase = 300
for c in customers:
    tier = c["tier"]
    rate = tier_discounts.get(tier, 0)
    discount_amount = test_purchase * rate
    print(f"Name: {c['name']} | Tier: {tier} | Discount: ${discount_amount:.2f}")


# EXERCISE 7 · Intermediate: Nested catalog
print("\n--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for item_name, data in catalog.items():
    if data["stock"] < 20:
        print(f"LOW STOCK ALERT: {item_name} has only {data['stock']} units left!")


# EXERCISE 8 · Advanced: Sales by region
print("\n--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

region_summary = {}
for tx in transactions:
    region = tx["region"]
    amount = tx["amount"]
    region_summary[region] = region_summary.get(region, 0) + amount

for region in sorted(region_summary.keys()):
    print(f"{region}: {region_summary[region]}")
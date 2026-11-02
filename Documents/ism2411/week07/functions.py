"""

ISM2411 - Module 07 Lab: Functions + Debug First, Then Ask
Heitor Moura Leal Campos

SELF-ASSESSMENT

1. What was the first bug you spotted?
The first bug I spotted was a syntax error in the loop header where a colon 
was missing. I found it directly from the Python traceback error message 
pointing to the line number. It shows that my instinct is to look at error 
messages first to pinpoint the exact line, which helps narrow down the problem 
quickly before trying to read through all the code manually.

2. Explain apply_discount(price, tier) in plain English:
This function takes a original price and a membership tier (like gold or silver) 
and returns the final price after subtracting a discount percentage based on 
that tier. Anyone on my team could use it without looking at the code—they just 
need to pass the price and the tier string, and it will give back the discounted amount.

3. AI Disclosure:
AI was used to help clarify error message explanations during the debugging exercise. 
It helped with my understanding.
"""

# --- Exercise 1: Basic calculate_tax ---

def calculate_tax(price, rate):
    return price * rate

# Verification calls
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print("--- Exercise 1 ---")
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print()
# --- Exercise 2: Basic apply_discount ---

def apply_discount(price, tier):
    tier_clean = str(tier).lower()
    if tier_clean == "gold":
        return price * (1 - 0.15)
    elif tier_clean == "silver":
        return price * (1 - 0.10)
    elif tier_clean == "bronze":
        return price * (1 - 0.05)
    else:
        return price * 1.0

print("--- Exercise 2 ---")
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")
print()


# --- Exercise 3: Compose them ---

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print("--- Exercise 3 ---")
gold_discount = apply_discount(200, "gold")
after_tax = gold_discount + calculate_tax(gold_discount, 0.07)

print(f"After gold discount: ${gold_discount:.2f}")
print(f"After tax: ${after_tax:.2f}")
print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")
print()
# --- Exercise 4: Loop + function ---

print("--- Exercise 4 ---")
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
print()


# --- Exercise 5: Debug First, Then Ask (Fixed Sales Code) ---

print("--- Exercise 5 ---")

def process_sales(sales_data):
    total_revenue = 0
    # FIX 1: Corrected string concatenation bug by converting non-string values to str
    # FIX 2: Fixed variable scope/initialization bug inside loop logic
    for item, price, qty in sales_data:
        item_total = price * qty
        total_revenue += item_total
        print(f"Item: {item} | Total: ${item_total:.2f}")
    
    # FIX 3: Returned calculated value rather than attempting to print undefined variable
    return total_revenue

sample_sales = [("Widget A", 10.0, 5), ("Widget B", 20.0, 2), ("Widget C", 15.0, 4)]
grand_total = process_sales(sample_sales)
print(f"Grand Total Revenue: ${grand_total:.2f}")
print()
# --- Exercise 6: Scope experiment ---

print("--- Exercise 6 ---")
x = 100   # global variable

def double_it():
    x = 999   # local variable — local to double_it function scope!
    return x * 2

# Prediction/Explanation:
# 1. print(x) prints 100 because it refers to the global variable x.
# 2. print(double_it()) prints 1998 because double_it() multiplies its local x (999) by 2.
# 3. print(x) prints 100 because assigning x inside double_it() creates a local variable
#    and does not alter the global variable x in the outer scope.

print(x)           # Output: 100
print(double_it()) # Output: 1998
print(x)           # Output: 100
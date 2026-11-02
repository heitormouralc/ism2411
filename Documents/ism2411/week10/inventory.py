"""
Reflection:
1. What is the most surprising thing about how lists work in Python compared to what you expected coming in?
Python lists are extremely flexible and dynamic, allowing you to store different data types and modify elements easily without needing to declare fixed sizes in advance. The ease of using built-in methods like append and sort makes manipulation much more intuitive.

2. Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.
In a daily sales tracking and promotional discount scenario, managing hundreds of records manually in Excel would require complex formulas and time-consuming filters. With a list and a simple loop in Python, you could filter and recalculate all prices automatically in fractions of a second.
"""

# EXERCISE 1 · Beginner: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# EXERCISE 2 · Beginner: Index practice
middle_index = len(inventory) // 2
print(inventory[0])
print(inventory[-1])
print(inventory[middle_index])

# EXERCISE 3 · Beginner: Slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# EXERCISE 4 · Intermediate: Modify
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# EXERCISE 5 · Intermediate: Tuple comparison
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught: Tuples are immutable and protect coordinates from accidental modification.")
print(coords)

# EXERCISE 6 · Intermediate: Average of a list of sales
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)
print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_day} | Worst: {worst_day}")

# EXERCISE 7 · Intermediate: Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for p in prices:
    discounted.append(round(p * 0.90, 2))
print(prices)
print(discounted)

# EXERCISE 8 · Advanced: Filter above threshold
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = [s for s in sales_data if s > 300]
high_avg = sum(high_sales) / len(high_sales) if high_sales else 0
print(f"{high_sales} | Count: {len(high_sales)} | Avg: ~{round(high_avg, 2)}")
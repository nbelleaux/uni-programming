"""
This file contains the code for the Week 3 Lab exercises, focusing on for loops, while loops, and GitHub integration.
"""

for i in range(20):
    if i % 2 == 0:
        print(i + 2)

        costs = [5.99, 15.49, 23.75, 9.99, 12.50]




total_cost = 0
for cost in costs:
    total_cost += cost
    print(f"Added {cost}, the total is now {total_cost:.2f}")
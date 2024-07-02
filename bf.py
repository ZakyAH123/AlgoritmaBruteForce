import time
import random

def knapsack_brute_force(capacity, n):
    def helper(capacity, n):
        print(f"knapsack_brute_force({capacity},{n})")
        if n == 0 or capacity == 0:
            return 0, []

        elif weights[n-1] > capacity:
            return helper(capacity, n-1)

        else:
            include_item_value, include_item_list = helper(
            capacity - weights[n-1], n-1)
            include_item_value += values[n-1]
            include_item_list = include_item_list + [n-1]

            exclude_item_value, exclude_item_list = helper(capacity, n-1)

            if include_item_value > exclude_item_value:
                return include_item_value, include_item_list
            else:
                return exclude_item_value, exclude_item_list

    max_value, items = helper(capacity, n)
    return max_value, items

values = [random.randint(1, 1000) for _ in range(40)]
weights = [random.randint(1, 50) for _ in range(40)]
capacity = 100
n = len(values)

start_time = time.time()
max_value, items = knapsack_brute_force(capacity, n)
end_time = time.time()
elapsed_time = end_time - start_time

print("\nMaximum value in Knapsack =", max_value)
print("Items included in the Knapsack:", items)
print(f"Time taken to run: {elapsed_time:.4f} seconds")

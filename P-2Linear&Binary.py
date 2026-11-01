Create P-2 linear and binary search
# Customer account IDs
customer_ids = [102, 205, 150, 123, 301, 110, 175]


# A. Linear Search
def linear_search(customer_list, target_id):
    for i in range(len(customer_list)):
        if customer_list[i] == target_id:
            return True

    return False


# B. Binary Search
def binary_search(sorted_list, target_id):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == target_id:
            return True

        elif sorted_list[mid] < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return False


# Sort the customer IDs for Binary Search
sorted_ids = sorted(customer_ids)

# Input customer ID
search_id = int(input("Enter Customer ID to search: "))


# Test Linear Search
found_linear = linear_search(customer_ids, search_id)

if found_linear:
    print("Linear Search: Found")
else:
    print("Linear Search: Not Found")


# Test Binary Search
found_binary = binary_search(sorted_ids, search_id)

if found_binary:
    print("Binary Search: Found")
else:
    print("Binary Search: Not Found")
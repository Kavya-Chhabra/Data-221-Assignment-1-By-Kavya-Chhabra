#Question 4 (1 Point): Sorted Search with Conditions
#Given a list of random values between 0 and 1 and a random value x:
#Sort the list.
# Find all indices where the list value is greater than or equal to x.
#Print the sorted list, the value of x, and the first matching index (if one exists).

from random import random

# generate a list of 20 random values between 0 and 1
list_of_random_values_between_zero_and_one= [random() for numbers_generated in range(20)]

# generate a random comparison value x between 0 and 1
comparison_value_x = random()

# sort the list of random values in ascending values
list_of_sorted_random_values = sorted(list_of_random_values_between_zero_and_one)

#initialize the variable to store the first matching inde
first_index_where_value_is_greater_or_equal_to_x = None

#loop through the sorted list with both index and value
for current_index, current_value in enumerate(list_of_sorted_random_values):

    #check if the current value is greater than or equal to x
    if current_value >= comparison_value_x:
        first_index_where_value_is_greater_or_equal_to_x = current_index
    break  #stop after finding the first matching index
    
#print the sorted list
print("sorted list:", list_of_sorted_random_values)

#print the value of x
print("Value of x:", comparison_value_x)

#print the first matching index if it exists
if first_index_where_value_is_greater_or_equal_to_x is not None:
    print(
        "First index where value is greater than or equal to x:",
        first_index_where_value_is_greater_or_equal_to_x
    )
else:
    print("No value in the list is greater than or equal to x.")



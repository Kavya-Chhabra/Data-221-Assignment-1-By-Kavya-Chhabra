#Define a function that receives a list of numbers and returns a dictionary where:
#• Each key is a unique value from the list.
#• Each value is the percentage of elements in the list that are less than or equal to that key.
#The resulting dictionary should be sorted by key before being returned.

def distribution_analysis(list_of_numbers):

#Dictionary that will store each unique value and its percentage
    distribution_dictionary = {}

# total number of elements in the list
    total_number_of_elements_in_the_list = len(list_of_numbers)

#Get all unique values from the list and sort them
    sorted_unique_values = sorted(set(list_of_numbers))

#Loop through each unique value
    for current_unique_value in sorted_unique_values:

    #count how many values in the list are less than or equal to the current key
        count_less_than_or_equal_to_the_current_key = 0

        for current_number in list_of_numbers:
            if current_number <= current_unique_value:
                count_less_than_or_equal_to_the_current_key += 1

        # Calculate the percentage of values less than or equal to the current key
        percentage_less_than_or_equal = (
            count_less_than_or_equal_to_the_current_key /  total_number_of_elements_in_the_list

        ) * 100

    # Store the percentage in the dictionary
        distribution_dictionary[current_unique_value] = percentage_less_than_or_equal

    # Dictionary is already sorted because keys were processed in sorted order
    return distribution_dictionary


numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(numbers))



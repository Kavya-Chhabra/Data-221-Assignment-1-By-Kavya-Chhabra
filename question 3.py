#Define a function that computes xy. Then, given a list of pairs (x, y):
# • Use a for loop with argument unpacking to call the function.
# • Skip any pair where the exponent y is negative.
# • Store the valid results in a list and print the list

#this function calculates x to the power of y
def calculate_base_raised_to_exponent(base_value,exponent_value):
    return base_value ** exponent_value #mathematical logic


list_of_base_and_exponent_value_pairs = [[5,2], [3,-1], [4,3], [2,0]] #example list from assignment

list_of_valid_exponentiation_results = []# empty list to store valid results

#loop through each pair using argument unpacking
for base_value,exponent_value in list_of_base_and_exponent_value_pairs:
    if exponent_value < 0: # if the exponent is negative
        continue # skip this pair and move on to the next

    #calculate the exponentiation and store the result
    exponentiation_result = calculate_base_raised_to_exponent(
            base_value,
            exponent_value
        )

    #call the function and store the result
    list_of_valid_exponentiation_results.append(calculate_base_raised_to_exponent(base_value,exponent_value))

#print all the valid results
print(list_of_valid_exponentiation_results)

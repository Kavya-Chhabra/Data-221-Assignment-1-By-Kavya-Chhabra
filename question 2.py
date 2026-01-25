#Define a function that receives a list of strings and returns a dictionary with the following structure:
#• Each key is a string from the list.
#• Each value is another dictionary containing:
#– The length of the string
#– Whether the length is even or odd

#this function takes a list of strings and returns a dictionary where each string is mapped to its length and whether or not that length is even or odd
def create_dictionary_containing_length_and_parity_information_for_each_string(list_containing_input_strings):

    #this dictionary will store each string as a key and its information as the value
    dictionary_mapping_each_string_to_its_information = {}

    #loop through each string in the input list
    for current_string_from_input_list in list_containing_input_strings:

        #find the length of the current string
        length_of_current_string_from_input_list = len(current_string_from_input_list)

        #determine if the length of the string is even or odd
        parity_of_current_string_length = "even" if length_of_current_string_from_input_list % 2 == 0 else "odd"

        #store the length and parity information for the current string
        dictionary_mapping_each_string_to_its_information[current_string_from_input_list] = {
             "length": length_of_current_string_from_input_list,  # fixed: use the correct variable
             "parity": parity_of_current_string_length
        }

    #return the completed dictionary
    return dictionary_mapping_each_string_to_its_information

# Example test
list_containing_example_strings = ["data", "science"]

print(create_dictionary_containing_length_and_parity_information_for_each_string(list_containing_example_strings))

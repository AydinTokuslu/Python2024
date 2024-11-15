# Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
# Write a code that generates a list of the following numbers from
# the nested list above – 34, 67, 78. Your output should be another
# list:
# [34, 67, 78]. The list output should not have duplicates.

nested_list = [[12, 34, 56, 67], [34, 68, 78]] # Flatten the nested list and filter out the desired numbers
flattened_list = [item for sublist in nested_list for item in sublist]
desired_numbers = [34, 67, 78]
output_list = list(set([num for num in flattened_list if num in desired_numbers]))
# Sort the list to get the desired order
output_list.sort()
print(output_list)
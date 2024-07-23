def find_largest_number(input_list):
    if len(input_list) == 0:
        return "List is empty"
    else:
        largest = input_list[0]
        for num in input_list:
            if num > largest:
                largest = num
        return largest

# Example usage
numbers = [3, 7, 2, 10, 5]
print(find_largest_number(numbers))  # Output: 10

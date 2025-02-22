def reverse_string(s):
    return s[::-1]  # Using slicing to reverse the string

# Taking user input
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)

# Displaying the reversed string
print(f"Reversed string: {reversed_string}")

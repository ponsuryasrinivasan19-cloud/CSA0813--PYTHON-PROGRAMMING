# Take input from user
user_input = input("Enter elements separated by space: ")

# Convert input string to list
arr = user_input.split()

# Reverse manually
reversed_arr = []
i = 0
while i < len(arr):
    reversed_arr.insert(0, arr[i])
    i += 1

# Print reversed array
print("Reversed array:")
for element in reversed_arr:
    print(element)

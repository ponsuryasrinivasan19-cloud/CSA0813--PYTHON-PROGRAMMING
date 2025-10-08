nums = [1, 2, 3, 2, 4, 2, 5]
x = int(input("Enter element to remove: "))

while x in nums:
    nums.remove(x)

print("Updated list:", nums)

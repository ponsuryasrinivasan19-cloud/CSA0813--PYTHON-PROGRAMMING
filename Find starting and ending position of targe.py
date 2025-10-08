nums = [5,7,7,8,8,10]
target = 8

start = end = -1
for i, val in enumerate(nums):
    if val == target:
        if start == -1:
            start = i
        end = i
print([start, end])

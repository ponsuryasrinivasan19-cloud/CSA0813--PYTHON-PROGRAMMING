nums = [0,1,4,4,6,7]
k = 4
rotated = nums[-k:] + nums[:-k]
print(rotated)

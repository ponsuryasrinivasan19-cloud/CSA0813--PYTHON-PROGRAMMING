n = int(input("Enter number: "))
sq = n * n
d = len(str(n))
right = sq % (10**d)
left = sq // (10**d)
print((left + right) == n)

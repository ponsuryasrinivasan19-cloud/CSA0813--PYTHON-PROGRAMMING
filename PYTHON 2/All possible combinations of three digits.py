from itertools import permutations

digits = [1, 2, 3]
for p in permutations(digits):
    print(*p)

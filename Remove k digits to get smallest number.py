num = "1432219"
k = 3
stack = []

for digit in num:
    while k and stack and stack[-1] > digit:
        stack.pop()
        k -= 1
    stack.append(digit)

final = "".join(stack[:-k] if k else stack).lstrip('0')
print(final if final else "0")

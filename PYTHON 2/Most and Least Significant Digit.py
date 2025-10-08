num = int(input("Enter a number: "))
lsb = num % 10  # Least significant digit
msb = int(str(num)[0])  # Most significant digit
print(f"LSB: {lsb} & MSB: {msb}")

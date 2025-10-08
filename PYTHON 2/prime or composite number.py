def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_count = 0
composite_count = 0

for num in numbers:
    if num > 1:
        if is_prime(num):
            prime_count += 1
        else:
            composite_count += 1

print("Number of prime numbers:", prime_count)
print("Number of composite numbers:", composite_count)

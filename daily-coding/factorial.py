def fibonacci_of(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)

result = fibonacci_of(2)
print(result)
for n in range(15):
    print(fibonacci_of(n))
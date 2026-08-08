number = int(input())
total = 0

for i in range(1, number + 1):
    if number % i == 0:
        total += i

print(total)

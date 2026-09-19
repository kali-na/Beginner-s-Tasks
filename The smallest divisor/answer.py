number = int(input())
min = None

for i in range(2, number + 1):
    if number % i == 0:
        min = i
        break

print(i)

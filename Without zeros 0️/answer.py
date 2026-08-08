total = 1

for i in range(1, 11):
    number = int(input())
    if number > 0 or number < 0:
        total *= number

print(total)

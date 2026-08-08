n = int(input())
total = 0

# Перебираем только числа, оканчивающиеся на 5
for i in range(5, n + 1, 10):
    total += i

print(total)

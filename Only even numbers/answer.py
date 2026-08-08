all_even = True

for _ in range(10):
    x = int(input())
    if x % 2 != 0:
        all_even = False
        # break  # можно раскомментировать, если допустимо не вводить оставшиеся числа

if all_even:
    print('YES')
else:
    print('NO')

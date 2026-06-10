number_user = int(input())


if (number_user % 100) % 10 == 0 and (number_user % 100) // 10 == 0:
    print('YES')
else:
    print('NO')


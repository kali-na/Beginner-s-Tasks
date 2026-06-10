user_name = int(input())

if user_name % 2 != 0:
    print('YES')
elif 2 <= user_name <= 5:
    print('NO')
elif 6 <= user_name <= 20:
    print('YES')
else:  # user_name > 20 и при этом чётное
    print('NO')

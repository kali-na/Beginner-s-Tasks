number = int(input())

if number == 0:
    print('зеленый')
elif number == 1 or number == 3 or number == 5 or number == 7 or number == 9 or number == 12 or number == 14 or number == 16 or number == 18 or number == 19 or number == 21 or number == 23 or number == 25 or number == 27 or number == 30 or number == 32 or number == 34 or number == 36:
    print('красный')
elif number == 2 or number == 4 or number == 6 or number == 8 or number == 10 or number == 11 or number == 13 or number == 15 or number == 17 or number == 20 or number == 22 or number == 24 or number == 26 or number == 28 or number == 29 or number == 31 or number == 33 or number == 35:
    print('черный')
else:
    print('ошибка ввода')

number = int(input())

one = number // 1000
two = (number // 100) % 10
three  = (number % 100) // 10
four = ((number % 1000) % 100) % 10

if one + four == two - three:
    print('ДА')
else:
    print('НЕТ')

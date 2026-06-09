number_user = int(input())

first_n = number_user // 100
second_u = (number_user // 10) % 10
third_m = number_user % 10

print('Сумма цифр =', first_n + second_u + third_m)
print('Произведение цифр =', first_n * second_u * third_m)

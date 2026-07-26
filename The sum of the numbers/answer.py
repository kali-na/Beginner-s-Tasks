number_user = int(input("Привет, введи число, сколько раз будешь набирать чисел: "))

count = 0
for i in range(number_user):
    numbers_user = int(input("Введи число: "))
    count += numbers_user

print("Сумма ваших чисел равна:", count)

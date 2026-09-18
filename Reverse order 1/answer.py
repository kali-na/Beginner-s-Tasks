user_number = int(input("Привет, напиши любое число: "))


while user_number != 0:
    last_digit = user_number % 10
    print(last_digit)

    user_number = user_number // 10

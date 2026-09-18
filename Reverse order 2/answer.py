user_number = int(input())

while user_number != 0:
    last_digit = user_number % 10
    print(last_digit, end='')

    user_number = user_number // 10
    

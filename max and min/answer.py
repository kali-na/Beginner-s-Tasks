user_name = abs(int(input()))

if user_name == 0:
    print("Максимальная цифра:", 0)
    print("Минимальная цифра:", 0)
else:
    max_digit = -1
    min_digit = 10

    while user_name != 0:
        last_digit = user_name % 10
        if last_digit > max_digit:
            max_digit = last_digit
        if last_digit < min_digit:
            min_digit = last_digit
        user_name //= 10

    print("Максимальная цифра равна", max_digit)
    print("Минимальная цифра равна", min_digit)

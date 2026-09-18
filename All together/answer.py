user_number = int(input())
sum = 0
quantity = 0
multiplication = 1
last_num = user_number % 10

while user_number != 0:

    last_digit = user_number % 10

    sum += last_digit
    quantity += 1
    multiplication *= last_digit

    user_number = user_number // 10

print(sum)
print(quantity)
print(multiplication)
print(float(sum / quantity))
print(last_digit)
print(last_digit + last_num)

import math

number_user = int(input())

count = 0
for i in range(1, number_user + 1):
    count += (1 / i)

print(count - math.log(number_user))

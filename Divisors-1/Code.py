number = int(input())

def count_divisors(user_number):
    count = 0

    for i in range(1, user_number + 1):
        if user_number % i == 0:
            count += 1
    return '+' * count

for j in range(1, number + 1):
    print(f"{j}{count_divisors(j)}")

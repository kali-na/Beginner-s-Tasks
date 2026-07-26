number_start = int(input())
number_finish = int(input())

count = 0
for i in range(number_start, number_finish + 1):
    if i % 10 == 4:
        count += 1
    elif i % 10 == 9:
        count += 1

print(count)

import statistics
number_user = int(input())

one_number = number_user // 100
two_number = (number_user // 10) % 10
three_number = number_user % 10

max_number = max(one_number, two_number, three_number)
min_number = min(one_number, two_number, three_number)

numbers = [one_number, two_number, three_number]
average_number = statistics.median(numbers)

if max_number - min_number == average_number:
    print('Число интересное')
else:
    print('Число неинтересное')

import statistics
number_one, number_two, number_three = int(input()), int(input()), int(input())

numbers = [number_one, number_two, number_three]

max_number = max(numbers)
min_number = min(numbers)
average_number = statistics.median(numbers)

print(max_number)
print(average_number)
print(min_number)

first_city, second_city, third_city = input(), input(), input()

data_len = [len(first_city), len(second_city), len(third_city)]

if len(first_city) < len(second_city) and len(first_city) < len(third_city):
    print(first_city)
elif len(second_city) < len(first_city) and len(second_city) < len(third_city):
    print(second_city)
elif len(third_city) < len(first_city) and len(third_city) < len(second_city):
    print(third_city)

if len(first_city) > len(second_city) and len(first_city) > len(third_city):
    print(first_city)
elif len(second_city) > len(first_city) and len(second_city) > len(third_city):
    print(second_city)
elif len(third_city) > len(first_city) and len(third_city) > len(second_city):
    print(third_city)

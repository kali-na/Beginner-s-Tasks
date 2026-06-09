first_num, second_num, third_num = int(input()), int(input()), int(input())

if first_num == second_num == third_num:
    print('Равносторонний')
elif first_num == second_num or second_num == third_num or third_num == first_num:
    print('Равнобедренный')
else:
    print('Разносторонний')

s1 = input()
s2 = input()
s3 = input()

lengths = [len(s1), len(s2), len(s3)]
lengths.sort()

# Проверяем, является ли последовательность арифметической прогрессией:
# разность между 2-м и 1-м элементом должна равняться разности между 3-м и 2-м
if lengths[1] - lengths[0] == lengths[2] - lengths[1]:
    print("YES")
else:
    print("NO")

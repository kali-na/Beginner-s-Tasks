a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# Находим границы пересечения
left = max(a1, a2)
right = min(b1, b2)

if left < right:
    # Есть отрезок
    print(left, right)
elif left == right:
    # Есть одна общая точка
    print(left)
else:
    # Пустое множество
    print("пустое множество")

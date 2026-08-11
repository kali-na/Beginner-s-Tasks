name = input()
alex_pos = -1
levon_pos = -1
count = 0

while name != "":
    count += 1
    if name == "Александра":
        alex_pos = count
    elif name == "Левон":
        levon_pos = count

    # Если оба имени уже найдены, можно прекращать чтение (но для простоты оставим до конца ввода)
    if alex_pos != -1 and levon_pos != -1:
        # Можно добавить break, если ввод гарантированно заканчивается после Левона
        pass

    try:
        name = input()
    except EOFError:
        break

# Между ними — разница позиций минус 1 (сами Александра и Левон не считаются)
print(levon_pos - alex_pos - 1)

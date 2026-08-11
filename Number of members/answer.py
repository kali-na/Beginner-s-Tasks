words = 0

word = input()
while word != "стоп" and word != 'хватит' and word != 'достаточно':
    words += 1
    word = input()

print(words)

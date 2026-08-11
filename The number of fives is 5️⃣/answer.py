sums = 0

word = int(input())
while (word > 0) and (word < 6):
    if word == 5:
        sums += 1
    word = int(input())

print(sums)

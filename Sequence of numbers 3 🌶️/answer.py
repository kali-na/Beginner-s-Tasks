numberStart = int(input())
numberFinish = int(input())

for i in range(numberStart, numberFinish - 1, -1):
    if i % 2 != 0:
        print(i)

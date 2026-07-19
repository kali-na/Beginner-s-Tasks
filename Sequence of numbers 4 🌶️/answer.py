numberStart = int(input())
numberFinish = int(input())

if numberStart <= numberFinish:
    for i in range(numberStart, numberFinish + 1):
        print(i)
elif numberStart > numberFinish:
    for b in range(numberStart, numberFinish - 1, -1):
        print(b)

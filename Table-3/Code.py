n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):          # всегда до 9 включительно
        print(f"{i} + {j} = {i + j}")
    print()

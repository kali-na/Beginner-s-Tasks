m = int(input())  # стартовое количество организмов
p = int(input())  # среднесуточное увеличение в процентах
n = int(input())  # количество дней

population = m

for day in range(1, n + 1):
    print(day, population)
    population += population * p / 100  # рост по формуле сложного процента

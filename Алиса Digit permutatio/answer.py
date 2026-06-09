number = int(input())

d1 = (number // 10 ** 2) % 10
d2 = (number // 10 ** 1) % 10
d3 = (number // 10 ** 0) % 10

print(d1, d2, d3, sep="")
print(d1, d3, d2, sep="")
print(d2, d1, d3, sep="")
print(d2, d3, d1, sep="")
print(d3, d1, d2, sep="")
print(d3, d2, d1, sep="")

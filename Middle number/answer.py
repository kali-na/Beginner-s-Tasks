one, two, three = int(input()), int(input()), int(input())

if one < two < three or three < two < one:
    print(two)
elif two < one < three or three < one < two:
    print(one)
elif one < three < two or two < three < one:
    print(three)

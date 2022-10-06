a = int(input())
b = 1
while b <= a:
    c = 1
    while c <= a:
        print(b * c, end="\t")
        c += 1
    b += 1
    print()

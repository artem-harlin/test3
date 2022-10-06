summ = int(input('$'))
money = [64, 32, 16, 8, 4, 2, 1] 
for x in money:
    while summ >= x: print(x, end=" "); summ -= x

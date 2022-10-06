a = int(input())
sum = 1
curr = 1
for i in range(2, a + 1):
    curr *= i
    sum += curr
print(sum)

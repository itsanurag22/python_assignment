n = input()
x = list(map(int, input().split()))
x.sort(reverse = True)
sum = 0
hSum = 0
c=0
for i in x:
    sum += i
for j in range(0, len(x)):
    hSum += x[j]
    sum -= x[j]
    c += 1
    if(hSum > sum):
        break
if(int(n) == len(x)):
    print(c)




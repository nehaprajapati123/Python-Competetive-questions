sum= 0
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        sum = sum+i
print(sum)
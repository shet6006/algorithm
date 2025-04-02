sum=0
i=1
x=int(input())
while sum+i<x:
    sum= sum+i
    i+=1
a=x-sum
b=i-a+1
if i%2==0:
    print(f"{a}/{b}")
else:
    print(f"{b}/{a}")


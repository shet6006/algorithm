n,m=map(int, input().split())
salt=n*0.07
water=n+m
result=int((salt/water)*10000)
print(f"{result/100:.2f}")
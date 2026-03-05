import math
def solution(arr):
    
    def gcd(a,b):
        while b>0:
            a, b = b, a%b
        return a
    
    c = 1
    for i in arr:
        c = (i*c)//gcd(i,c)
    
    return c
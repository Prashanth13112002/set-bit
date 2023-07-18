def setbit(a,b):
    if(a!=b):
        return 2**a+2**b
    else:
        return 2**a
a=int(input())
b=int(input())
print(setbit(a,b))
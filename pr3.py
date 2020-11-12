import math
a=int(input("Introdu a : "))
b=int(input("Introdu b: "))
if ((a>b)or(a==b)):
    print("nu corespunde conditiei")
else:
    l=round(math.log(n,m))
    if (a**l==b):
        print(b,"este o putere a lui",a)
    else:
        print(b,"nu este o putere a lui",a)
        
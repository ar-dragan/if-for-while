n=int(input("Introdu numărul: "))
s=1
s2=1
h=0
for i in range(1,n+1):
    s=s*2+i
print("a)Cand Mihai a împlinit",n,"ani, a primit",s,"dolari")
while s2<=100:
    h+=1
    s2=s2*2+h
print("b)Cadoul lui Mihai a fost mai mare de 100$,când a împlinit",h,"ani")
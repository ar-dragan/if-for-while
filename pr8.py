a=int(input("dati un numar pozitiv:"))
b=int(input("dati un numar pozitiv:"))
c=int(input("dati un numar pozitiv:"))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("Este un triunghi cu astfel de laturi")
    if a!=b and b!=c and a!=c:
        print("Triunghuil este scalen")
    elif a==b and a==c and b==c:
        print("Triunghiul este echilateral")
    else:
        print("Triunghiul este isoscel")
else:
    print("Nu este un triunghi cu astfel de laturi")
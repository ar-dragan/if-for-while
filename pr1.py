"""
Se dă numărul natural n,n={28,29,30,31}. Să se afișeze denumirile lunilor cu numărul de zile n. De exemplu, pentru n=30, se va afișa: aprilie,
iunie,septembrie,noiembrie.
"""
n=int(input("Introdu numărul: "))
if ((n<28)or(n>31)):
    print("Nu sunt luni cu asa numar de zile")
elif n==28:
    print("februarie, daca nu e an bisect")
elif n==29:
    print("februarie, daca e an bisect")
elif n==30:
    print("aprilie,iunie,septembrie,noiembrie")
else:
    print("ianuarie,martie,mai,iulie,august,octombrie,decembrie")
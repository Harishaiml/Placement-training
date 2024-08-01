n=int(input("Enter Marked price:"))
if n<=7000:
    a=n*(10/100)
    e=n-a
    print(e)
elif n>7000 and n<=10000:
    b=n*(15/100)
    f=n-b
    print(f)
elif n>10000:
    c=n*(20/100)
    g=n-c
    print(g)

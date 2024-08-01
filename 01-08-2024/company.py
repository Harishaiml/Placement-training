n=int(input("Enter your year:"))
m=int(input("Enter salary:"))
if n>=2 and n<4:
    a=m*(4/100)
    d=m+a
    print(d)
elif n>=4 and n<8:
    b=m*(7/100)
    e=m+b
    print(e)
elif n>=8:
    c=m*(10/100)
    f=m+c
    print(f)

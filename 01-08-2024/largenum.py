a=int(input("Enter a :\n"))
b=int(input("Enter b :\n"))
c=int(input("Enter c :\n"))
print(max(a,b,c))

if a==b & a>c:
   print("Equal number are large ",a)
elif b==c &b>a:
   print("Equal number are large ",b)
elif c==a & c>b:
   print("Equal number are large ",c)
elif a==b & b==c:
    print("All number are equal")

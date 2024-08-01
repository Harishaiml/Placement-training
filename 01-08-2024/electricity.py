a=int(input("Enter unit "))
if a<=100:
    print("No charge")
elif a>=100 and a<=200:
    print((a-100)*5)
elif a>200:
    print((a-200)*10+100*5)

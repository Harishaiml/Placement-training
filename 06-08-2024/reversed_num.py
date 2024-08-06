def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"The reversed number is: {reversed_num}")

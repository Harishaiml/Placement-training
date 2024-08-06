def is_prime_trial_division(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
num = 29
if is_prime_trial_division(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

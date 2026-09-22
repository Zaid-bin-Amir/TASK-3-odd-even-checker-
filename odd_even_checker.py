def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from user
num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"{num} is {result}")
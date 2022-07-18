try:
    number = int(input("Enter any number: "))
    if number % 2 == 0 and number % 4 != 0:
        print(f"The number {number} is even number ")
    elif number % 4 == 0 and number % 2 == 0:
        print(f'The number {number} is even and multiple of 4 ')
    elif number % 2 != 0:
        print(f"The given number {number} is Odd! ")
    else:
        print("The number is not even nor odd it's is zero ")
    num = int(input("Enter any number to divide by check: "))
    check = int(input("Enter the divisor number: "))
    if num % check == 0:
        print(f"The number {num} is divide evenly by {check} ")
    else:
        print("The number is not divide by evenly by check! ")
except ValueError:
    print("Wrong input please try again! ")
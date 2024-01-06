# check if prime
def check_prime(number):
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for x in range(2, number):
            if number % x == 0:
                is_prime = False
    return is_prime


is_on = True
print("Check for a prime number!")
while is_on:
    input_num = input("Enter an integer: ")
    try:
        num = int(input_num)
        if isinstance(num, int):  # if integer check prime
            if check_prime(num):
                print(str(num) + " is a prime number.")
            else:
                print(str(num) + " is not a prime number.")
            is_on = False
    except ValueError:
        print("Please enter a valid integer.")

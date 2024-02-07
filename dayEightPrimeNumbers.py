# Program to check if a number is prime or not

num = int(input("EnterNumber: "))

# define a flag variable
isNotPrime = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:          
            isNotPrime = True            
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
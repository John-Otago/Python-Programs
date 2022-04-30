# Prime number
# A common beginner exercise

# A simple solution:


while True:
    num = int(input("Please enter a whole number: "))

    if num > 1:
        for i in range(2, (num//2+1)):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else: # This is where I tend to make a mistake--I often incorrectly put "else" within the for loop.
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

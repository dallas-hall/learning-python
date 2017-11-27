# The Collatz Sequence
# define the function with 1 parameter
def collatz(input):
    # try to cast the paramater to an int
    try:
        number = int(input)
    # catch any non-int inputs
    except ValueError:
        print('The input was not an integer.')
        # exit after printing the error message
        return None
    # check if the number is greater than or equal to 1
    if number >= 1:
        # check if even
        if number % 2 == 0:
            # integer division by 2
            number = (number // 2)
        # check if odd
        elif number % 2 == 1:
            # integer division by 3
            number = (number // 3)
        # check if the answer is 1
        if number == 1:
            # if it is 1 we are done
            print('We are done, 1 has been reached')
        # if it isn't, call the function again
        else:
            print('Answer was ' + str(number) + ', starting the sequence again.')
            # recursive call
            collatz(number)
    # catch numbers < 1
    else:
        print('The inputted number needs to be >= 1')
        return None

print('Enter a number.')
userNumber = input()
collatz(userNumber)

        
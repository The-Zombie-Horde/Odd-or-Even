import sys


def check_odd_or_even(number):
    if number % 2 == 1:
        num = 'odd'
    elif number % 2 == 0:
        num = 'even'
    else:
        print('Did you even give me a number? Or did you not follow instructions?  ')
        sys.exit()
    return num


num = float(input('Instructions:  Give me a positive integer!    '))
num1 = check_odd_or_even(num)
print('You gave me an {} number: {}'.format(num1, int(num)))

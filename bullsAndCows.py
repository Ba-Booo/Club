import random

correctNumbers = []

while len(correctNumbers) < 3:

    randomNumber = random.randint(0, 9)

    if randomNumber not in correctNumbers:

        correctNumbers.append( randomNumber )

print("\n")

while True:

    strike = 0
    ball = 0
    out = 0

    for n in range( 1, 4 ):

        print( n, "번째 숫자 : ", end = "" )
        inputNumber = int( input() )

        if inputNumber == correctNumbers[ n - 1 ]:

            strike += 1 

        elif inputNumber in correctNumbers:

            ball += 1 

        else:

            out += 1

    print("\n스트라이크: ", strike, "\n볼\t  : ", ball, "\n아웃\t  : ", out, "\n")

    if strike == 3:

        break


print("\033[35m", "~", "\033[31m", "C", "\033[33m", "★", "\033[32m", "L", "\033[36m", "★", "\033[34m", "E", "\33[35m", "★", "\033[31m", "A", "\033[33m", "★", "\033[32m", "R", "\033[36m", "~", "\n")
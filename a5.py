import random
num = random.randint(1, 10)
while 0==0:
    print('Guess a number between 1 and 10')
    print('if you guess less than 7 times you won')
    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!!')
        break
    elif i < num:
               print('Try Higher')
    elif i > num:
               print('Try Lower')


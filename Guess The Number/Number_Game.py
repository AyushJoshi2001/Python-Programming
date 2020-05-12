import random
print('*******GUESS THE NUMBER*******')
print('******************************')

random_no = random.randint(1,20)

while (True):
    print('Guess the Number : ', end = '')
    guess = int(input())

    if (guess > random_no):
        print('Wrong Answer! Try a smaller Number.')
    elif (guess < random_no):
        print('Wrong Answer! Try a greater Number.')
    else:
        print('Congratulations! You guessed the right Number.')
        break

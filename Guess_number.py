import random

def guess_number():
    x = int(input(f'Please input number that duration of your number :between 1 to : '))
    random_num = random.randint(1,x)
    guess = 0
    cnt=0
    while guess!=random_num:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess<random_num:
            print('Oh sorry, guess again. Your number is low, guess ...')
        elif guess>random_num:
            print('Oh sorry, guess again. Your number is high, guess ...')
        cnt=cnt+1
    
    print(f'Yesss, congrate, You have guessed the number {random_num} correctly!!, your guess after {cnt} times')

def computer_guess():
    x = int(input(f'Please input number that duration of your number :between 1 to : '))
    low = 1
    high = x
    answer = ''
    cnt =0
    while answer != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        answer = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if answer == 'h':
            high = guess - 1
        elif answer == 'l':
            low = guess + 1
        cnt=cnt+1

    print(f'Yesss,The computer guessed your number , {guess}, correctly after {cnt} times')   

guess_number()

import random
import os
import os.path
from time import sleep


def Show():
    print('1. Play')
    print('2. View Results')
    print('3. Quit')

    choice = int(input('\nEnter your choice:\t'))
    Choice(choice)


def Choice(ch):
    choice = ch

    if choice == 3:
        print('Thanks For Coming !!!')
        sleep(2)
        exit(0)

    elif choice == 1:
        Play()
        while True:
            replay = input('\nWanna Play Again ?(YES/NO)\t')
            if replay == 'NO' or 'no' or 'No':
                break
            else:
                Play()

    elif choice == 2:
        if not os.path.isfile('D:/PyGames/NGG.txt'):
            print('\nNo Result Found.\nYou are the first Player.\n')

        else:
            f = open('D:/PyGames/NGG.txt')
            print(f.read())
            f.close()

    else:
        print('Please enter a valid choice.')

    Show()


def Play():
    name = input('\nEnter your full Name:\t')
    upper_limit = int(input('\nEnter the upper limit:\t'))
    lower_limit = int(input('Enter the lower limit:\t'))

    generated_number = random.randint(lower_limit, upper_limit)

    attempt = 1

    while attempt <= 5:
        print('\nRemaining Chances:\t', 5 - attempt)
        print('Lower Limit:\t', lower_limit)
        print('Upper Limit:\t', upper_limit)

        guessed_number = int(input("\nEnter your guess in the range of upper and lower limit:\t"))

        if guessed_number == generated_number:
            print('Correct !')
            break

        elif guessed_number > generated_number:
            print('Guessed number is big.')
            attempt += 1

        else:
            print('Guessed number is small.')
            attempt += 1

    if attempt < 6:
        print(name, 'guessed the number in ', attempt, 'attempts.')
    else:
        print('OOPS !!! Maximum attempt reached.\nDon\'t Worry, You can try again.')
        print('\nThe correct number was\t', generated_number)

    Record(name, attempt)


def Record(name, attempt):
    if not os.path.isdir('D:/PyGames'):
        os.mkdir('D:/PyGames')

    if not os.path.isfile('D:/PyGames/NGG.txt'):
        f = open('D:/PyGames/NGG.txt', 'x')
        f.close()

    if attempt > 5:
        f = open('D:/PyGames/NGG.txt', 'a')
        f.write('%s could not guessed the number in 5 attempts.\n' % name)
        f.close()

    elif attempt <= 5:
        f = open('D:/PyGames/NGG.txt', 'a')
        f.write('%s Guessed the number in %d attempts.\n' % (name, attempt))
        f.close()


Show()

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
        print('\nThanks For Coming !!!')
        sleep(2)
        exit(0)

    elif choice == 1:
        Play()
        while True:
            replay = input('\nWanna Play Again ?(YES/NO)\t')
            if replay == 'NO' or 'no' or 'No' or 'nO' or 'n' or 'N':
                break
            elif replay == 'Y' or 'y' or ' YES' or 'yes' or 'Yes':
                Play()

    elif choice == 2:
        if not os.path.isfile('D:/PyGames/NGG.txt'):
            print('\n\nNo Result Found.\nYou are the first Player.\n')

        else:
            print()
            f = open('D:/PyGames/NGG.txt')
            print(f.read())
            f.close()

    else:
        print('\nPlease enter a valid choice.')

    Show()


def Play():
    while True:
        name = input('\nEnter your full Name:\t')
        if not all(x.isalpha() or x.isspace() for x in name):
            print("\nEnter a valid name.")
        else:
            break

    while True:
        lower_limit = input('\nEnter the lower limit:\t')
        if not lower_limit.isnumeric():
            print('Enter positive numbers only.')
        else:
            lower_limit = int(lower_limit)
            break

    while True:
        upper_limit = input('\nEnter the upper limit:\t')
        if not upper_limit.isnumeric():
            print('\nEnter positive numbers only.')
        elif int(upper_limit) <= lower_limit:
            print('\nUpper Limit should be greater than lower limit.')
        else:
            upper_limit = int(upper_limit)
            break

    generated_number = random.randint(lower_limit, upper_limit)

    attempt = 0

    while attempt < 5:
        print('\nAttempts in hand:\t', 5 - attempt)
        print('Lower Limit:\t', lower_limit)
        print('Upper Limit:\t', upper_limit)

        guessed_number = input("\nEnter your guess in the range of upper and lower limit:\t")
        if not guessed_number.isnumeric():
            print('\nEnter numbers only.')
            continue
        else:
            guessed_number = int(guessed_number)

        if guessed_number > upper_limit or guessed_number < lower_limit:
            print('\nEnter the Number in the limits provided.')
            continue

        elif guessed_number == generated_number:
            print('\nCorrect !')
            break

        elif guessed_number > generated_number:
            print('\nGuessed number is big.')
            attempt += 1

        else:
            print('\nGuessed number is small.')
            attempt += 1

    if attempt < 5:
        print(name, 'guessed the number in ', attempt + 1, 'attempts.')
    else:
        print('\nOOPS !!! Maximum attempt reached.\nDon\'t Worry, You can try again.')
        print('\nThe correct number was\t', generated_number)

    Record(name, attempt + 1)


def Record(name, attempt):
    if not os.path.isdir('D:/PyGames'):
        os.mkdir('D:/PyGames')

    if not os.path.isfile('D:/PyGames/NGG.txt'):
        file = open('D:/PyGames/NGG.txt', 'x')
        file.close()

    file = open('D:/PyGames/NGG.txt')
    lines = file.readlines()

    if len(lines) == 5:
        file = open('D:/PyGames/NGG.txt')
        lines = file.readlines()
        file.close()

        del lines[0]

        new_file = open('D:/PyGames/NGG.txt', 'w+')
        for line in lines:
            new_file.write(line)
        new_file.close()

    file.close()

    if attempt > 5:
        f = open('D:/PyGames/NGG.txt', 'a')
        f.write('%s could not guessed the number in 5 attempts.\n' % name)
        f.close()

    else:
        f = open('D:/PyGames/NGG.txt', 'a')
        f.write('%s Guessed the number in %d attempts.\n' % (name, attempt))
        f.close()


# Main Function Calling Show()
Show()

from db import db_matcher
import sys

while True:

    print('Welcome to the very first version of this fabulous book recommender.')
    print('Importing database...')
    score = db_matcher()

    user_input = str(input('Please describe what would you like to read about. \
                    \nEvery word counts!\n'))
    while True:
        n_cats_desired = input('How many recommendations do you wish to display?\n (1-10)\n')
        if int(n_cats_desired) in [1,2,3,4,5,6,7,8,9,10]:
            break
    
    print('Matching results...')
    score.match(user_input, int(n_cats_desired))
    print('Matching done!\n')
    score.get_result()

    while True:
        choice = int(input('Enter recommendation index to see the book description\n \
            or enter 42 to exit\n'))
        if choice == 42:
            break
        else:
            score.get_detail(choice)

    while True:
        answer = str(input('Run again? y/n: \n'))
        if answer in ('y','n'):
            break
        print('invalid input, try again, its not that hard')

    if answer == 'y':
        continue
    else:
        sys.exit('cya nerd')
        



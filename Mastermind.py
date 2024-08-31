# Mastermind
import random
colors = ['Red','Yellow','Blue','Green','Orange','Pink','Purple','Cyan','Silver','Teal']
lwcolors = []
randomcolors = []
guesses = []
count = 0
penalty = 0
name = input('What is your name?')

print('The code maker is here. Available colors are')

for i in colors:
    if i != colors[-1]:
        print(i, end = ', ')

    else:
        print(i)
        print('You have 15 guesses, total of 5 penalties are allowed but avoid penalties.')
        print('The code maker selected 4 colors')
        print('You can start guessing', name)

for y in colors:
    lwcolors.append(y.lower())

a = 0
while a != 4:
    x = random.randint(0,9)
    if lwcolors[x] not in randomcolors:
        rc = lwcolors[x]
        randomcolors.append(rc)
        a = a + 1

#print(randomcolors)
while count != 15:
    if penalty == 5:
        print('You have reached the maximum amount of penalties, You Lose')
        quit()
    count = count + 1
    print('this is guess number', count)
    guesses = []
    for b in range(1,5):
        print('Enter color number', b, end = ' ')
        guess = input('')
        guess = guess.strip()
        print(guess)
        guesses.append(guess.lower())
    
    #print(guesses)
    for c in guesses:
        contin = False
        l = len(guesses)
        if c == '':
            l = l - 1
        elif guesses.count(c) > 1 and c not in lwcolors:
            print('Sorry', name, ' cannot recognize the colors you entered and repeated colors are not allowed in this game. One penalty is considered')
            penalty = penalty + 1
            print('Total penalties=', penalty)
            break
        elif l != 4:
            print('Sorry', name, ', you have not entered enough colors. One penalty is considered')
            penalty = penalty + 1
            print('Total penalties=', penalty)
            break
        elif guesses.count(c) > 1 and c in lwcolors:
            print('Sorry', name, ', repeated colors are not allowed in this game. One penalty is considered')
            penalty = penalty + 1
            print('Total penalties=', penalty)
            break
        elif c not in lwcolors and guesses.count(c) == 1:
            print('Sorry', name, ' cannot recognize the colors you entered. One penalty is considered')
            penalty = penalty + 1
            print('Total penalties=', penalty)
            break

        else:
            contin = True
    
    correct = False
    while correct == False and contin == True:
        black = 0
        white = 0

        for p in range(0,4):
            if guesses[p] == randomcolors[p]:
                black = black + 1

            if guesses[p] != randomcolors[p] and guesses[p] in randomcolors:
                white = white + 1

        print('You got', black, 'black, and', white, 'white for this guess')

        if guesses == randomcolors:
            print('You won the game with', count, 'guesses and', penalty, 'penalties, Congratulations')
            quit()
            
        if guesses != randomcolors:
            print('Incorrect, Try again!')
            break
    if count == 15:
        print('You are out of guesses, You Lose')
        quit()
        
            
        






    
    
    
    
    
    

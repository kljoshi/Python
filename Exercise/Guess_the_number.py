# Guess the Number Game
# library that includes randint() function which generates random number
import random
number = random.randint(1,20)

# Prompt User to guess a number between 1 and 20
print('I am thinking of a number between 1 and 20.')

# counter variable to count the number of guesses made by the user
counter = 0

# while condition to loop n number of times until correct guess is made or 0 is selected
while True:
    
    print('Take a guess. To exit press 0.')
    guess = int(input())
    counter = counter + 1

    if(guess == int(0)):
        print('Your have exited the game. The number was ' + str(number) + '.')
        print('Thank you for playing.')
        break
    elif(guess == number):
        print('Good job! You guessed my number in ' + str(counter) + ' guesses!')
        break
    elif(guess > number):
        print('Your Guess is Too high')
    elif(guess < number):
        print('Your Guess is Too low')

    
    

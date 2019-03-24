def game():
        import random

        print('Hello, stranger. What is your name?')
        name = input ()

        print('Well, ' + name + ', guess how many cats I own. Ok, to make it easier I can tell you it is more than 1 and less than 20.')
        CatNumber = random.randint(1,20)

 #       print('DEBUG: Cat Number is ' + str(CatNumber))

        for guessesTaken in range(1,7):
                try:
                        print('Take a guess!')
                        guess = int(input())

                except ValueError:
                        print('What is this trickery?! Use an actual number, you rascal!')
                        continue

                if guess < 0:
                        print("I do not own any negative cats.")

                if guess > 20:
                        print("You must be taking me for a total Crazy Cat Lady.")
                        
                else:
                        if guess < CatNumber:
                            print('Not enough cats!')
                        elif guess > CatNumber:
                            print('Too many cats!')
                        else:
                            break
        if guess == CatNumber:
            print('Not too bad, ' + name + ' you guessed in ' + str(guessesTaken) + ' guesses.')
            
        else:
            print('Nope. I have ' + str(CatNumber) + ' cats.')

while True:
    game()
    print('Wanna play again? (type \'y\' for yes, and \'n\' for no\)')
    exitgame = input()

    if exitgame == 'n':
        break


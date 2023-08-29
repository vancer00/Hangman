from hangmanlist import wordList
import time
import random
badGuess = 0
gameWordList = []
gameWord = random.choice(wordList)
guessedLettersList = []
x = 0
guessLetter = ""
playerName = ""
playerDecision = ""

def hangman_graphic(badGuess, playerName, playerDecision):
    if badGuess == 0:
        print("   _____")
        print("   |   |")
        print("   |   ")
        print("   |   ")
        print("   |   ")
        print("   |   ")
        print("-------")
    elif badGuess == 1:
        print("   _____")
        print("   |   |")
        print("   |   O")
        print("   |   ")
        print("   |   ")
        print("   |   ")
        print("-------")
        print("1 Wrong Guess, %s" % playerName)
    elif badGuess == 2:
        print("   _____")
        print("   |   |")
        print("   |   O")
        print("   |   |")
        print("   |   |")
        print("   |   ")
        print("-------")
        print("2 Wrong Guesses, %s" % playerName)
    elif badGuess == 3:
        print("   _____")
        print("   |   |")
        print("   |   O")
        print("   |   |")
        print("   |   |")
        print("   |  /")
        print("-------")
        print("3 Wrong Guesses, %s" % playerName)
    elif badGuess == 4:
        print("   _____")
        print("   |   |")
        print("   |   O")
        print("   |   |")
        print("   |   |")
        print("   |  / \\")
        print("-------")
        print("4 Wrong Guesses, %s" % playerName)
    elif badGuess == 5:
        print("   _____")
        print("   |   |")
        print("   |   O")
        print("   |  /|")
        print("   |   |")
        print("   |  / \\")
        print("-------")
        print("5 Wrong Guesses %s. One more and the stick hangs!" % playerName)
    else:
        print("   _____")
        print("   |   |")
        print("   |   O")
        print("   |  /|\\")
        print("   |   |")
        print("   |  / \\")
        print("-------")
        print("%s, you have failed this poor stick figure miserably." % playerName)
        print("You make your final guess and their body swings in the breeze.")
        playerDecision = input('Would you like to restart? y/n: ')

def doeswordcontain(x, guessLetter, gameWord, guessedLettersList):
    for i in range(len(gameWord)):
        if guessLetter == gameWord[x]:
            gameWordList[x] = guessLetter
            x += 1
        else:
            x += 1
    x = 0
    guessedLettersList.append(guessLetter)
    print("_______________________")
    print("Guessed Letters:")
    print(*guessedLettersList)
    print("_______________________")

for i in range(len(gameWord)):
    gameWordList.append("_")

print("Welcome to Hangman, where your guesses decides a stick figure's fate")
playerName = input("What's your name?: ")
print("Glad to have you playing %s. Let's begin!" % playerName)

def coregame(gameWordList, badGuess, guessLetter, playerName, gameWord, guessedLettersList):
    while gameWordList.__contains__('_') and badGuess < 6:
        print(*gameWordList, sep='|')
        hangman_graphic(badGuess, playerName, playerDecision)
        guessLetter = input("Enter a letter: ")
        doeswordcontain(x, guessLetter, gameWord, guessedLettersList)
        if guessLetter not in gameWord:
            badGuess += 1
        else:
            badGuess += 0

#while gameWordList.__contains__('_'):
#    hangman_graphic(badGuess, playerName)
#    guessLetter = input("Enter a letter: ")
#    doeswordcontain(x, guessLetter, gameWord, guessedLettersList)
#    if guessLetter not in gameWord:
#        badGuess += 1
#    else:
#        badGuess += 0
#    print(*gameWordList, sep='|')
coregame(gameWordList, badGuess, guessLetter, playerName, gameWord, guessedLettersList)

if "_" not in gameWordList:
    print("You have won! The word was %s" % gameWord)
    playerDecision = input('Would you like to restart? y/n: ')
    if playerDecision in ("y", "n"):
        if playerDecision == "y":
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            coregame(gameWordList, badGuess, guessLetter, playerName, gameWord, guessedLettersList)
        else:
            print("Thank you for giving it a shot!")
            time.sleep(5)
            quit()
    else:
        print("Invalid Response and I am not sure how to get it to redo the if statement.")
        time.sleep(2)
        print("You will now continue to the exit.")
        time.sleep(2)
elif "_" in gameWordList:
    print("You have failed miserably! The word was %s" % gameWord)
    playerDecision = input('Would you like to restart? y/n: ')
    if playerDecision in ("y", "n"):
        if playerDecision == "y":
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            coregame(gameWordList, badGuess, guessLetter, playerName, gameWord, guessedLettersList)
        else:
            print("Thank you for giving it a shot!")
            time.sleep(5)
            quit()
    else:
        print("Invalid Response and I am not sure how to get it to redo the if statement.")
        time.sleep(2)
        print("You will now continue to the exit.")
        time.sleep(2)
else:
    print("I'm not sure how this happened, but you made it.")
    time.sleep(1)
    print("The game will close in 5 seconds")
    time.sleep(5)
    quit()

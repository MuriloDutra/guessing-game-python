import guessingGame
import formattingNumbers

print("*****")
print("FILES")
print("*****")

print("(1) guessingGame.py (2) formattingNumbers.py")

chosen_file = int(input("Choose a file: "))

if(chosen_file == 1):
    guessingGame.play()
elif(chosen_file == 2):
    formattingNumbers.format()

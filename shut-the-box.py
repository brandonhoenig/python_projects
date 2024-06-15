import random
import string
import time
numbers_on_board = list(range(1,13))# Create the board. 
print("Welcome to Shut The Box!")
time.sleep(3)# adds time between welcome statment and game. 
while True:# game while statement. 
    if numbers_on_board == []:
        print("You shut the box!")
    elif numbers_on_board != []: 
        time.sleep(1) # adds time
        dice_roll = random.randint(1,6) + random.randint(1,6) # rolls dice
        print("Rolling dice...")
        time.sleep(1) 
        print("You rolled", dice_roll)
        print("You have these numbers left to remove:\n", numbers_on_board)
        first_number_to_remove = input("Which number do you want to remove first? Hit Enter/Return if no possible choices.\n") # pick number to come off board first. 
        while True:
            if first_number_to_remove == '':
                print("Reopen the program to play again!")
                time.sleep(2)
                exit()
            elif int(first_number_to_remove) not in numbers_on_board:
                print("This number is not an option. Try again.\n")
            elif dice_roll == int(first_number_to_remove):
                numbers_on_board.remove(int(first_number_to_remove))
                break
            elif dice_roll < int(first_number_to_remove):
                print("This number is not an option. Try again.\n")
            elif dice_roll > int(first_number_to_remove):
                numbers_on_board.remove(int(first_number_to_remove))
                second_number_to_remove = input("Which number do you want to remove second? Hit Enter/Return if no possible choices.\n")
            if second_number_to_remove == '':
                print("Reopen the program to play again!")
                time.sleep(2)
                exit()
            elif int(second_number_to_remove) not in numbers_on_board:
                print("This number is not an option. Try again.\n")
            elif dice_roll != int(first_number_to_remove) + int(second_number_to_remove):
                print("This number is not an option. Try again.\n")
            elif int(second_number_to_remove) in numbers_on_board and int(second_number_to_remove) != int(first_number_to_remove) and int(second_number_to_remove) + int(first_number_to_remove) == dice_roll:
                numbers_on_board.remove(int(second_number_to_remove))
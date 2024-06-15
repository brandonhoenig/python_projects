import random
import time

while True:
    try:
        want_to_play = input("Want to play Shut the Box? Answer yes or no.\n")
        numbers_on_board = list(range(1,13))
        if want_to_play.lower()== 'yes':
            print("Great! Let's play!")
            while True:
                if numbers_on_board == []:
                    print("You shut the box!")
                    break
                else:
                    print(numbers_on_board)
                    dice_roll_1 = random.randint(1,6) # rolls dice
                    dice_roll_2 = random.randint(1,6) # rolls dice
                    print("You rolled...")
                    print("[",dice_roll_1,"]", "[",dice_roll_2,"]")
                    if dice_roll_1 + dice_roll_2 > 0:
                        first_number_to_remove = int(input("Which number do you want to remove first? Hit Enter/Return if no possible choices.\n")) # pick number to come off board first.
                        if first_number_to_remove == dice_roll_1 + dice_roll_2:
                            numbers_on_board.remove(first_number_to_remove)
                        elif first_number_to_remove not in numbers_on_board:
                            print("Sorry, that is not an option. Open the game to try again.")
                            break
                        elif first_number_to_remove > dice_roll_1 + dice_roll_2:
                            print("That is not an option. Try again")
                        elif first_number_to_remove < dice_roll_1 + dice_roll_2:
                            second_number_to_remove = int(input("Which number do you want to remove second? Hit Enter/Return if no possible choices.\n")) # pick number to come off board first.
                            if second_number_to_remove not in numbers_on_board:
                                print("Sorry, that is not an option.")
                            elif second_number_to_remove == dice_roll_1 + dice_roll_2 - first_number_to_remove:
                                numbers_on_board.remove(second_number_to_remove)
                                numbers_on_board.remove(first_number_to_remove)
                            elif dice_roll_1 + dice_roll_2 != first_number_to_remove + second_number_to_remove:
                                print('Sorry, that is not an option. Open the game to try again.')
                                break
        elif want_to_play.lower()== 'no':
            print("Okay! Let's play again later!")
            time.sleep(1)
            pass
        else:
            print("I'm sorry. I don't understand.")
            continue
    except:
        pass
    else:
        break
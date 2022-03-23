"""
-----------------------------------------------
 Kaylas Game.
 Game Created By Adel Magdy Abd El-Hay
 latest update: 23 Mar. 2022
-----------------------------------------------
Game:
"""
import time

# Take from the user the name of two players.
Player1 = input("player1, Type your name please: ")
Player2 = input("player2, Type your name please: ")

# Display the rules of game.
print("\nRules: ")
print("you have the choice to play twice time or one time")
print("The numbers you can choose from is 1 --> 20")

# Sleep the program to give the user chance to read all rule.
time.sleep(0.75)
# Display the winning condition.
print("\nThe winning Condition:")
print("The winner who choose the last number", "\n")

# Sleep the program to give the user chance to read winning condition.
time.sleep(1)
# List of game from 1 to 20 (from 1 --> 9, from 0 --> 9 "10 --> 19", and the last 0 for 20 ).
print("list of game:")
list_Game = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(list_Game)

# "temp_list" which used in the final to check Who the winner.
temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# "Who_Play" to know who the last player play.
Who_Play = 0

# Function for the Player1 turn.
def Player1_Fuction():
    # to use these variables inside and outside the function.
    global Choice1_1
    global Choice1_2

    # Display who has to play in this turn.
    print(f"\n{Player1}: ")
    # Take from the player1 the inputs.
    [Choice1_1, Choice1_2] = (int(input("Enter the first choice : ")),\
    int(input("Enter the second choice, if you do not need choice, please enter 30 : ") if len(temp_list) != 1 else 1))

    # Check if the Choice1_1 is valid or not and if it is not valid tell the user to play again.
    if len(temp_list) != 0:
        Choice1_1 = Choice1_1 - 1

        while list_Game[Choice1_1] == "_":
            print("\nFirst")
            Choice1_1 = int(input("invalid Choice.\nplease Enter the first choice again 'another choice' :")) - 1

        # Remove the choice1_1 of the user and add in the same place in "list_Game" this '_'.
        list_Game.pop(Choice1_1)
        list_Game.insert(Choice1_1, "_")
        # Remove from the "temp_list" the choice1_1.
        temp_list.remove(Choice1_1 + 1)

    """
    Check if the user input Choice1_2 or not (and) is the choice2 valid or not and if it isn't valid tell the user to 
    play again.
    """
    if Choice1_2 != 30 and len(temp_list) != 0:
        Choice1_2 = Choice1_2 - 1

        while list_Game[Choice1_2] == "_":
            print("\nSecond")
            Choice1_2 = int(input("invalid Choice.\nplease Enter the second choice again 'another choice' :")) - 1

        # Remove the choice1_2 of the user and add in the same place in "list_Game" this '_'.
        list_Game.pop(Choice1_2)
        list_Game.insert(Choice1_2, "_")
        # Remove from the "temp_list" the choice1_2.
        temp_list.remove(Choice1_2 + 1)

    # Display the "list_Game" with the changes on it.
    print(f"\nlist of game:\n{list_Game}")

    # To use this variable inside and outside the function.
    global Who_Play
    # assign on the var "Who_Play" the value of 'player1'(the name  of player1).
    Who_Play = Player1


# Function for player2 turn.
def Player2_Function():
    # to use these variables inside and outside the function.
    global Choice2_1
    global Choice2_2

    # Display who has to play in this turn.
    print(f"\n{Player2}: ")
    [Choice2_1, Choice2_2] = (int(input("Enter the first choice : ")),\
    int(input("Enter the second choice, if you do not need choice, please enter 30 : ") if len(temp_list) != 1 else 1))

    # Check if the Choice2_1 is valid or not and if it is not valid tell the user to play again.
    if len(temp_list) != 0:
        Choice2_1 = Choice2_1 - 1

        while list_Game[Choice2_1] == "_":
            print("\nfirst")
            Choice2_1 = int(input("invalid Choice.\nplease Enter the first choice again 'another choice' :")) - 1

        # Remove the choice2_1 of the user and add in the same place in "list_Game" this '_'.
        list_Game.pop(Choice2_1)
        list_Game.insert(Choice2_1, "_")
        # Remove from the "temp_list" the choice2_1.
        temp_list.remove(Choice2_1 + 1)

    """
    Check if the user input Choice2_2 or not and is the choice2 valid or not and if it isn't valid tell the user to
    play again."""
    if Choice2_2 != 30 and len(temp_list) != 0:
        Choice2_2 = Choice2_2 - 1

        while list_Game[Choice2_2] == "_":
            print("\nSecond")
            Choice2_2 = int(input("invalid Choice.\nplease Enter the second choice again 'another choice' :")) - 1

        # Remove the choice2_2 of the user and add in the same place in "list_Game" '_'.
        list_Game.pop(Choice2_2)
        list_Game.insert(Choice2_2, "_")
        # Remove from the "temp_list" the choice2_2.
        temp_list.remove(Choice2_2 + 1)

    # Display the "list_Game" with the changes on it.
    print(f"\nlist of game:\n{list_Game}")

    # To use this variable inside and outside the function.
    global Who_Play
    # assign on the var "Who_Play" the value of 'player2'(the name  of player2).
    Who_Play = Player2

# Temp var to help me in make the game loop and check who the winner.
temp = True
while temp:
    # Call the function of player1
    Player1_Fuction()
    """
    Check if there is any number in 'temp_list' or not.
    if there is any number then Call the function of player2 if not continue the game 
    """
    if len(temp_list) != 0:
        Player2_Function()
    """
    Check if the game is finished or not if it is finished print who the winner and end game if not Call the function
    of player2 and continue the game.
    """
    if len(temp_list) == 0:
        print(f"\nThe winner is : {Who_Play}\n")
        temp = False
        break

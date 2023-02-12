# Import the modules
import logic
import os
from simple_colors import *

# Define the main function
if __name__ == '__main__': 
    matrix = logic.start_game()
    logic.add_number(matrix)
    while(input("Shall we start? (y): ") != "y"):
        print("Think abt it again... ", end="")
        pass
    os.system("cls")
    print(yellow("Here we go"))
    logic.print_game(matrix)
    statusCodes = {
        1: "Continue Playing",
        2: "Try someother move",
        3: "LOST",
        4: "WON"
	}

    # Main game loop
    while (True):
        x= input("Enter any command: ")
        os.system('cls')
        if(x == 'W' or x == 'w'):
            tempMatrix = matrix
            matrix, flag = logic.move_up(matrix)
            status = logic.get_current_state(matrix)
            print(status)
            if(status == statusCodes[1]):
                if(tempMatrix != matrix):
                    logic.add_number(matrix)
            elif(status == statusCodes[2]):
                pass
            else:
                break

        elif(x == 'S' or x == 's'):
            matrix, flag = logic.move_down(matrix)
            status = logic.get_current_state(matrix)
            print(status)
            if(status == statusCodes[1]):
                logic.add_number(matrix)
            elif(status == statusCodes[2]):
                pass
            else:
                break

        elif(x == 'A' or x == 'a'):
            matrix, flag = logic.move_left(matrix)
            status = logic.get_current_state(matrix)
            print(status)
            if(status == statusCodes[1]):
                logic.add_number(matrix)
            elif(status == statusCodes[2]):
                pass
            else:
                break

        elif(x == 'D' or x == 'd'):
            matrix, flag = logic.move_right(matrix)
            status = logic.get_current_state(matrix)
            print(status)
            if(status == statusCodes[1]):
                logic.add_number(matrix)
            elif(status == statusCodes[2]):
                pass
            else:
                break
        
        # Cheat codes
        elif(x =="sunTzu"):
            logic.multiply(matrix,2)
            status = logic.get_current_state(matrix)
            print(status)
            if(status == statusCodes[1]):
                pass
            elif(status == statusCodes[2]):
                pass
            else:
                break

        # Force Stop the game 
        elif(x=="stop"):
            break
                
        else:
            print("Invalid Key Pressed")
            
        logic.print_game(matrix)
        
        if(logic.get_current_state(matrix) == "LOST"):
            break
    
    stat = logic.get_current_state(matrix)
    if(stat == statusCodes[3]):
        os.system("cls")
        print(red("You have lost the game... PLease try again...", ["bright"]))
        logic.print_game(matrix)
        print("\n\n")
    elif(stat == statusCodes[4]):
        os.system("cls")
        print(green("Congragulations on your victory", ["bright"]))
        print(green("It was nice playing with you...", ["bright"]))
        logic.print_game(matrix)
        print("\n\n")
    elif(stat == statusCodes[1]):
        os.system("cls")
        print(cyan("Seems like the game has been quit... If you have any sugggestions on how the game can be improved, We are all ears", ["bright"]))
        print(magenta("Well anyway, see you again soon... Here is a copy of the gameboard before the game had been stopped..."))
        logic.print_game(matrix)
        print("\n")
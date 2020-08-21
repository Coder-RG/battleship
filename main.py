#!/usr/bin/env python3

from random import randint, choice
from ships import *
import sys
from time import sleep

#Text to help the player with the how-to of the game

def ui():
    """Includes How-to-play of the original board game.
       Just some stuff to be printed. Not much!"""

    print("Hello!")

    print("-------------Welcome to Battleships--------------")
    print(
    """"Instructions:
    1) You have to place your ships on a 10*10 square as you like
    and your opponent will do the same.

    2) Both the players have 5 ships of various lengths. You have to guess
    where the other person's ships are and if you guess correctly, you inflict
    damage to the opponents ship.

    3) First one to destroy other's ships wins!"""
    )

    print("-------------Various ships-------------------")
    print(
    """
    1) Carrier      <----- size 5,
    2) Battleship   <----  size 4,
    3) Destroyer    <---   size 3,
    4) Submarine    <---   size 3,
    5) Patrol Boat  <--    size 2
    """
    )

    return 0

# Display the map

def show_grid(lst):
    """Shows the grid on the screen"""

    print("\nPlacement of the ships\n")
    print("   0 1 2 3 4 5 6 7 8 9\n")
    for index, x in enumerate(lst):
        print(str(index), " ".join(map(str, x)), sep="  ")
    return 0


# List of all the ships and their size

list_ships = [
    ("Carrier", 5),
    ("Battleship", 4),
    ("Destroyer", 3),
    ("Submarine", 3),
    ("Patrol Boat", 2)
]

# Generates a 10*10 grid

def load_grid():
    """Creates a 10*10 grid for use later in the other functions"""

    lst = []
    for x in range(10):
        lst.append(['-','-','-','-','-','-','-','-','-','-'])
    return lst

# Player Interaction

def player(show):
    """UI for the input from the player for the co-ordinates of the ships"""

    print("-------------Let's begin then-------------------\n")
    print("This is how the 10*10 grid looks\n")
    lst = load_grid()
    grid_with_zero(lst)
    print("\nNow it is you turn to play:\n")
    p = Player(input("Enter your name:"))
    print("\nTry not to place the ships on the same place\n")
    for ship, size in list_ships:
        print(f"\nLet's place {ship} of size: {size}\n")
        s = Ships(ship, size)
        ship_placed = False
        while not ship_placed:
            r = int(input("Choose a value between 0-9 to choose the row:"))
            c = int(input("Choose a value between 0-9 to choose a column:"))
            o = input("Place horizontal(h) or vertical(v)?")
            if o == 'h':
                if c + s.size <= 9:
                    s.set_pos(r,r,c, c+s.size)
                    for grid_col in range(s.size):
                        lst[r][c] = 1
                        p.ship_coordinates.append((r,c))
                        c+=1
                    ship_placed = True
                else:
                    print("The size of the ship is too big, try again!")
            elif o == 'v':
                if r + s.size <= 9:
                    s.set_pos(r,r+s.size, c,c)
                    for grid_row in lst[r:r+s.size]:
                        grid_row[c] = 1
                        p.ship_coordinates.append((r,c))
                    ship_placed = True
                else:
                    print("The size of the ship is too big, try again!")
            else:
                print("Enter h or v for horizontal or vertical")
        p.dict_ships[ship] = s
    if show == 1:
        show_grid(lst)
    return p

# Generating values for computer ships

def comp(name, show):
    """Generates coordinates for the computer's ships"""

    print(f"\nWaiting for {name} to place their ships\n")
    sleep(1)
    lst = load_grid()
    p = Player(name)
    for ship, size in list_ships:
        s = Ships(ship, size)
        ship_placed = False
        while not ship_placed:
            r = randint(0,9)
            c = randint(0,9)
            o = choice(['h','o'])
            if o == 'h':
                if c + s.size <= 9:
                    s.set_pos(r,r,c, c+s.size)
                    for grid_col in range(s.size):
                        lst[r][c] = 1
                        p.ship_coordinates.append((r,c))
                        c+=1
                    ship_placed = True
                else:
                    continue
            else:
                if r + s.size <= 9:
                    s.set_pos(r,r+s.size, c,c)
                    for grid_row in lst[r:r+s.size]:
                        grid_row[c] = 1
                        p.ship_coordinates.append((r,c))
                    ship_placed = True
                else:
                    continue
        p.dict_ships[ship] = s
    if show == 1:
        show_grid(lst)
    sleep(1)
    return p

# Playing the game

def game(p1, p2):
    """This is where the actual gameplay resides"""
    win = False
    damage1 = 0
    damage2 = 0
    print("\nNow that both the players have their ships positioned, let's battle!\n")
    while not win:
        # Player1 or the human
        # x,y = map(int, input("Enter x,y coordinates").split())
        # if x in range(10) and y in range(10):
        #     if (x,y) in p2.ship_coordinates:
        #         print("Well done, That's a hit!")
        #         p2.ship_coordinates.remove((x,y))
        #     else:
        #         print("That was a miss. Better luch next time.")
        x,y = randint(0,9), randint(0,9)
        if (x,y) in p2.ship_coordinates:
            # print("Hit! Your damaged opponent's ship.")
            damage1 += 1
            p2.ship_coordinates.remove((x,y))
        else:
            # print("Miss! Better luck next time.")
            pass
        u,v = randint(0,9), randint(0,9)
        if (u,v) in p1.ship_coordinates:
            # print("Computer hit. Your ship was damaged.")
            damage2 += 1
            p1.ship_coordinates.remove((u,v))
        else:
            # print("Miss! Your ship didn't get damaged.")
            pass
        if not p1.ship_coordinates:
            print(f"{p2.player_name} won!")
            break
        elif not p2.ship_coordinates:
            print(f"{p1.player_name} won!")
            break
    return damage1, damage2


# Call the necessary functions

if __name__ == '__main__':
    if len(sys.argv) <= 4:
        if len(sys.argv) > 1:
            show, p1, p2 = sys.argv[1:]
        else:
            show, p1, p2 = 0, "Player1", "Player2"
    else:
        raise Exception("The max allowed number of arguments is 3")
    player1 = comp(p1, int(show))
    player2 = comp(p2, int(show))
    hits = game(player1, player2)
    sleep(1)
    print(f"\n{player1.player_name} hit {hits[0]} and {player2.player_name} hit {hits[1]}")

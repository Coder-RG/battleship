#!/usr/bin/env python3

def ui():

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

def grid(lst):
    print("\nThis is how the 10*10 grid looks\n")
    print("   0 1 2 3 4 5 6 7 8 9\n")
    for index, x in enumerate(lst):
        print(str(index), " ".join(map(str, x)), sep="  ")
    return 0


# Player interaction

def player():
    list_ships = ["Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boat"]
    print("-------------Let's begin then-------------------\n")
    print("This is how the 10*10 grid looks\n")
    lst = []
    for x in range(10):
        lst.append([0,0,0,0,0,0,0,0,0,0])
    print("   0 1 2 3 4 5 6 7 8 9\n")
    for index, x in enumerate(lst):
        print(str(index), " ".join(map(str, x)), sep="  ")

    print("\nNow it is you turn to play:\n")
    for ship in list_ships:
        print(f"Let's place {ship}:\n")
        while(True):
            r = int(input("Choose a value between 0-9 to choose the row:"))
            c = int(input("Choose a value between 0-9 to choose a column:"))
            o = input("Place horizontal(h) or vertical(v)?")
            lst[r][c] = 1
            break
        break
        grid(lst)
    return 0

if __name__ == '__main__':
    player()

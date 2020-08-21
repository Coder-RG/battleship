# Battleship: The Board Game

Many of you might have already played Battleship and there are many repositories
which have developed this game on various different platforms. However, I have
tried something new. This projects takes in name of the players as input and does
everything on its own.

#### Features of this project:
* It will automatically fill the board with ships,
* It will play the game for you and will announce the winner at the end,
* Gives how much damage each person dealt to the other.

##### Q. Reason why this is not interactive?<br>
A. Well the game is solely based in command-line and thus it won't be interesting
   to play the game on the command-line. However, if you want to see who has better
   luck between you and your friend, then this will tell without being biased.

##### Q. Why would this project be of any interest to you?<br>
A. The code for inputting from the user is all there and if you want you can fork
   this repository and do a better job than I did, maybe even add GUI to make it
   look appealing?

##### If you are still interested in this project why not try it yourself?

1. Run the code using python3 on command-line<br>
 - `python3 main.py`

2. Run the code after changing the permissions of the file( below code for linux)
 - `chmod +x main.py`
 - `./main.py`

3. Some things to remember
 - The file has 3 attributes: `python3 main.py {0|1} arg1 arg2`
 - {0|1}
 : means choose either 0 or 1. Choose 1 if you want to see the ship placements and 0 otherwise.
 - arg1
 : Name of player 1
 - arg2
 : Name of player 2
 - if you don't pass any arguments, the default are `0 Player1 Player2`

 Hope you like this repo and have fun playing with it.

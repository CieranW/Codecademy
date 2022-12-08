# Final Project(CS101): Terminal Game(Battleships)
import random as rd
from itertools import chain
# from icecream import ic


def playing_field():
    grid_count = 0
    full_grid = ""
    grid = "| A | B | C | D | E | F | G | H | I | J |\n"

    while grid_count < 11:
        full_grid += grid
        grid_count += 1
        if grid_count == 10:
            print(full_grid)


# Prints out a 10 x 10 grid:
# A0 A1 A2 A3 A4 A5 A6 A7 A8 A9
# B0 B1 B2 B3 B4 B5 B6 B7 B8 B9
# C0 C1 C2 C3 C4 C5 C6 C7 C8 C9
# D0 D1 D2 D3 D4 D5 D6 D7 D8 D9
# E0 E1 E2 E3 E4 E5 E6 E7 E8 E9
# F0 F1 F2 F3 F4 F5 F6 F7 F8 F9
# G0 G1 G2 G3 G4 G5 G6 G7 G8 G9
# H0 H1 H2 H3 H4 H5 H6 H7 H8 H9
# I0 I1 I2 I3 I4 I5 I6 I7 I8 I9
# J0 J1 J2 J3 J4 J5 J6 J7 J8 J9

rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
grid_id = []
for i in range(len(rows)):
    new_row = []
    for col in columns:
        row = rows[i]
        new_str = row + str(col)
        new_row.append(new_str)
    grid_id.append(new_row)

# Print out the list in a grid view


def print_grid(grid_id):
    return '\n'.join(''.join(str(i).center(4)for i in row) for row in grid_id)


# print(print_grid(grid_id))


# Random module will assign 5 ships randomised values from the grid
def ship_value(length):
    sv_count = 0
    ship = []
    while sv_count < length:
        #
        ship.append(rd.choice(list(chain.from_iterable(grid_id))))
        sv_count += 1
        if sv_count == length:
            return ship


# Test the randomiser of values to the length of ship.
ship1, ship2, ship3, ship4, ship5 = ship_value(4), ship_value(
    3), ship_value(1), ship_value(5), ship_value(2)


# Need to make sure that the values of the ships assigned are lined up, e.g. A0, A1, A2, A3 for a ship of length 4.

# Keep track of attempts, ships hit, score per ship hit
# Ship hit is 5 points, ship sunk is 20 points
# X amount of attempts to hit y amount of values worth of ships

# Create a class for the ship, has the attribute of length, etc. Method, can be hit.
def to_score():
    attempts = 0
    overall_score = 0
    # attempt = print(input("Enter a value (Ex:A8):\n"))
    ship_hit = []  # Player inputed the correct value that will contains a ship
    ship_sunk = []  # Player has succeeded in entering all the correct values associated with the ship
    while attempts < 20:
        for ship in ship_hit:
            print("Target hit!")
            overall_score += 5
            ship_hit.append(print_grid(grid_id))
            if len(ship) < 0:
                print("You have sunk a ship!")
                ship_sunk.append(print_grid(grid_id))
                overall_score += 20
        attempts += 1


player = input("Enter your name: ""\n")
print("Welcome, {}!".format(player), "\n")
choice = input("Are you ready to play? (Y/N)""\n")
yes = "Y"
no = "N"
if choice == no:
    print("That's too bad, {}:)".format(player), "\n")
elif choice != yes or choice != no:
    print("Value entered is incorrect! Please enter a correct value (Y/N).")
elif choice == yes:
    print("Fantastic! Let's get started, {}!".format(player), "\n")


def start_game():
    print("The aim of the game is simple.""\n")
    print("To win, you need to sink all of the battleship.""\n")
    print("There are 5 ships, ranging in length from 1 to 5.""\n")

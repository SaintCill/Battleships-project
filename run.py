import random


player_score = 0
computer_score = 0

# Starts off by creating board according to dimensions
def create_board(dims):
    return [["0" for _ in range(dims)] for _ in range(dims)]

# Function that prints the board itself, while also replacing ship positions with "0", so that they won't be revealed on the board.
def print_board(board):
    for row in board:
        row_str = []
        for cell in row:
            if cell == "S":
                row_str.append("0")
            else:
                row_str.append(cell)
        print(" ".join(row_str))

# Creates the ships themselves based on the dimensions given in later function, and gives them an orientation. 0 being vertical and 1 being horizontal.
# They are then given a position that we store inside of ship_locations
def ships(dims, amount):
    ship_locations = []
    for _ in range(amount):
        max_ship_length = min(int(dims), 5)
        len_ship = random.randint(2, max_ship_length)
        direction = random.randint(0, 1)
        if direction == 0:
            row = random.randint(0, dims - 1)
            col = random.randint(0, dims - len_ship)
            ship_coords = [(row, col + i) for i in range(len_ship)]
        else:
            col = random.randint(0, dims - 1)
            row = random.randint(0, dims - len_ship)
            ship_coords = [(row + i, col) for i in range(len_ship)]
        ship_locations.extend(ship_coords)
    return ship_locations

# Initializes the board and ship_locations.
def initialize_game(dims, amount):
    board = create_board(dims)
    ship_locations = ships(dims, amount)
    return board, ship_locations

# Takes in player input for row/col. The input is then checked to see if input is not a digit. If it is, the input is converted to an int
# and subracted by 1 to account for list orders starting from 0. The function will only return row/col if both values are greater 0, but less than dims
def player_guess(dims):
    while True:
        dims = int(dims)
        row_input = input("Row: ")
        col_input = input("Col: ")
        if not row_input.isdigit() or not col_input.isdigit():
            print("Invalid input. Please enter an input in number form (ie 5, 4, 1 etc)")
            continue
        row = int(row_input) - 1
        col = int(col_input) - 1
        if 0 <= row < dims and 0 <= col < dims:
            return (row, col)
        else:
            print(f"Invalid input. Please select a row and column between 1-{dims}.")

# Computer guesses a random combination between 0 and dims.
def computer_guess(dims):
    row = random.randint(0, int(dims) - 1)
    col = random.randint(0, int(dims) - 1)
    return (row, col)



# Handles updating the board. It checks if the player has guessed a combination of row/col, and if they have, prints a message to make player aware of this.
# If the coordinates have not been guessed, they are added to the list of coordinates already fired at.
def update_board(guess, board, ship_locations, guesses, player_turn=True):
    global player_score, computer_score
    if guess in guesses:
        print("You have already fired there.")
        return board, ship_locations
    guesses.append(guess)
    # Here we are giving row/col the values from the player/computer guess. Hit_ship then takes on the value true or false depending on if a row/col match is found.
    # If match is found and hit_ships is True, it replaces the 0 on the board with an X.
    row, col = guess
    hit_ships = [(ship_row, ship_col) for ship_row, ship_col in ship_locations if (row, col) == (ship_row, ship_col)]
    if hit_ships:
        if player_turn:
            player_score += 10
            print("Hit! You have discovered a space with a battleship!")
        else:
            computer_score += 10
            print("Enemy has hit one of our battleships!")
        board[row][col] = "X"
        # Here we create a copy of the ship_locations. This is to remove all instances of ships that exist on the guessed combination of row/col.
        # The copy of ship_locations is then returned instead of ship_locations, as i was running into an issue with a later while loop otherwise.
        ship_locations_copy = ship_locations[:]
        for hit_ship in hit_ships:
            ship_locations_copy.remove(hit_ship)
        return board, ship_locations_copy
    print("Miss!")
    return board, ship_locations

def play_again():
    answer = input("Would you like to play again? (yes/no): ").lower()
    return answer == "yes"

def welcome():
    print("Welcome to sink the battleship!")
    print("Hidden among the these coordinates, there is a battleship.")
    print("Select a row and column from 1 to 5 to guess where the battleship is located.")
    print("If you manage to sink all battleships, you win!")

def main():
    global player_score, computer_score
    while True:
        welcome()
        player_score = 0
        computer_score = 0
        # We begin by declaring a while loop where the user inputs dims. Dims is then checked to see if it is a number and if it is below 10.
        # If either conditions are not met, the user is prompted to input an actual number below 10.
        while True:
          try:
            dims_str = input("Enter the size for the board (2 = 2x2, 3 = 3x3 etc): ")
          except EOFError:
            print("EOFError occurred while reading input. Please provide valid input.")
            continue
          try:
            dims = int(dims_str)
          except ValueError:
            print("Please enter a valid number for the board size.")
            continue
          if not isinstance(dims, int):
            print("Invalid input. Please enter a valid number for the board size.")
            continue
          if dims >= 10:
            print("Please choose a board size under 10.")
            continue
          break


        amount = 4
        player_board, player_ship_locations = initialize_game(dims, amount)
        computer_board, computer_ship_locations = initialize_game(dims, amount)
        player_guesses = []
        computer_guesses = []

        while player_ship_locations and computer_ship_locations:
            print("Player radar:")
            print_board(player_board)
            print("\nEnemy radar:")
            print_board(computer_board)

            try:
              player_guess_coords = player_guess(dims)
              player_board, player_ship_locations = update_board(player_guess_coords, player_board, computer_ship_locations, player_guesses, player_turn=True)
            except EOFError:
              print("EOFError occured. Please provide valid input.")
              continue
          
            if not computer_ship_locations:
                break  # Exit the loop if the player wins

            computer_guess_coords = computer_guess(dims)
            computer_board, computer_ship_locations = update_board(computer_guess_coords, computer_board, player_ship_locations, computer_guesses, player_turn=False)

            if not player_ship_locations:
                break  # Exit the loop if the computer wins

        # Check if the player or computer has won
        if not computer_ship_locations:
            print("You have sunk all computer's battleships! You win!")
            player_score += 50
            print(f"Your final score was: {player_score} points!")
            print(f"Computer scored {computer_score} points!")
        elif not player_ship_locations:
            print("Computer has sunk all your battleships! You lose!")
            computer_score += 50
            print(f"Your final score was {player_score} points!")
            print(f"Computers final score was {computer_score} points!")

        if not play_again():
            break

main()

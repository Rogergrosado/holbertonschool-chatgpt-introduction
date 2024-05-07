# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Join elements of each row with " | " and print
        print("-" * 5)  # Print horizontal line between rows

# Function to check if there's a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":  # If all elements in a row are the same and not empty
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":  # If all elements in a column are the same and not empty
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":  # If elements in the main diagonal are the same and not empty
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":  # If elements in the secondary diagonal are the same and not empty
        return True

    return False

# Function to check if it's a tie
def check_tie(board):
    for row in board:
        if " " in row:  # If there's an empty space in any row
            return False
    return True  # If there's no empty space, it's a tie

# Main function for the Tic Tac Toe game
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]  # Initialize the board with empty spaces
    player = "X"  # Player starts with 'X'
    while not check_winner(board) and not check_tie(board):  # Continue the game until there's a winner or a tie
        print_board(board)  # Print the current board
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))  # Ask for row input
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))  # Ask for column input
            if board[row][col] == " ":  # If the selected spot is empty
                board[row][col] = player  # Place the player's symbol
                player = "O" if player == "X" else "X"  # Switch player
            else:
                print("That spot is already taken! Try again.")  # If the spot is already taken, ask again
        except (ValueError, IndexError):
            print("Invalid input! Please enter integers between 0 and 2.")  # Handle invalid input

    print_board(board)  # Print the final board
    if check_winner(board):  # If there's a winner
        print("Player " + player + " wins!")  # Print the winner
    else:
        print("It's a tie!")  # If it's a tie, print tie

# Start the game
tic_tac_toe()


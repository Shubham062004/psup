def print_board(board):
    # Loop through each row of the board
    for row in board:
        # Join the elements of the row with a pipe symbol and print them
        print("|".join(row))
        # Print a line of dashes to separate the rows
        print("-" * 9)

# A function to check if there is a winner 
def check_winner(board):
    # Check rows
    # Loop through each row of the board
    for row in board:
        # If the first element of the row is equal to the second and the third element, and is not a blank space
        if row[0] == row[1] == row[2] != " ":
            # Return the value of the first element, which is the winner
            return row[0]

    # Check columns
    # Loop through each column index of the board
    for col in range(3):
        # If the first element of the column is equal to the second and the third element, and is not a blank space
        if board[0][col] == board[1][col] == board[2][col] != " ":
            # Return the value of the first element, which is the winner
            return board[0][col]

    # Check diagonals
    # If the top-left element is equal to the middle and the bottom-right element, and is not a blank space
    if board[0][0] == board[1][1] == board[2][2] != " ":
        # Return the value of the top-left element, which is the winner
        return board[0][0]
    # If the top-right element is equal to the middle and the bottom-left element, and is not a blank space
    if board[0][2] == board[1][1] == board[2][0] != " ":
        # Return the value of the top-right element, which is the winner
        return board[0][2]

    # If none of the above conditions are met, return None, which means there is no winner yet
    return None

# A function to play the game
def play_game():
    # Create a board as a list of lists, each containing three blank spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Set the current player to "X"
    current_player = "X"
    # Set the winner to None
    winner = None

    # Loop until there is a winner
    while not winner:
        # Print the board
        print_board(board)
        # Ask the user to enter the row and column index where they want to place their mark
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # If the board at the given row and column is a blank space
        if board[row][col] == " ":
            # Place the current player's mark on the board
            board[row][col] = current_player
            # Check if there is a winner on the board
            winner = check_winner(board)
            # Switch the current player to the other player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        # If the board at the given row and column is not a blank space
        else:
            # Print an error message and ask the user to try again
            print("Invalid move. Try again.")

    # Print the final board
    print_board(board)
    # If there is a winner
    if winner:
        # Print the winner's mark
        print(f"{winner} wins!")
    # If there is no winner
    else:
        # Print a tie message
        print("It's a tie!")

# Call the function to start the game
play_game()
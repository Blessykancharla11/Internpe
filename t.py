def print_board(board):
    # Function to print the Tic Tac Toe board
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i*3 + j], "|", end=" ")
        print("\n-------------")

def check_winner(board):
    # Function to check if there's a winner
    rows = [[board[i*3 + j] for j in range(3)] for i in range(3)]
    columns = [[board[j*3 + i] for j in range(3)] for i in range(3)]
    diagonals = [[board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    lines = rows + columns + diagonals

    for line in lines:
        if line.count("X") == 3:
            return "X"
        elif line.count("O") == 3:
            return "O"
    return None

def play():
    # Function to play the Tic Tac Toe game
    board = ["-" for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)

        if check_winner(board):
            winner = check_winner(board)
            print(f"Player {winner} wins!")
            break
        elif "-" not in board:
            print("It's a tie!")
            break

        position = int(input("Enter a position (1-9): "))
        if position < 1 or position > 9 or board[position-1] != "-":
            print("Invalid move! Try again.")
            continue

        board[position-1] = current_player
        current_player = "O" if current_player == "X" else "X"

play()

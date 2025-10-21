# TASK 2: TIC-TAC-TOE AI

import math

# --- The Game Board and Logic ---

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    """Checks if the specified player has won."""
    # Check rows, columns, and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    """Checks if the board is full (tie condition)."""
    for row in board:
        if " " in row:
            return False
    return True

# --- The AI's Brain (Minimax Algorithm) ---

def minimax(board, depth, is_maximizing):
    """
    The core minimax algorithm.
    - `is_maximizing` is True if it's the AI's turn, False for the player's turn.
    - It returns a score for a given board state.
    """
    # Base cases: check for a terminal state (win, lose, tie)
    if check_winner(board, "O"):
        return 10 - depth  # AI wins
    if check_winner(board, "X"):
        return depth - 10  # Player wins
    if is_board_full(board):
        return 0  # Tie

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score = minimax(board, depth + 1, False)
                    board[r][c] = " "
                    best_score = max(score, best_score)
        return best_score
    else: # Minimizing player's turn
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, depth + 1, True)
                    board[r][c] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Finds the best possible move for the AI."""
    best_score = -math.inf
    best_move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "O"
                score = minimax(board, 0, False)
                board[r][c] = " "
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    return best_move

# --- Main Game Loop ---

def main():
    """The main function to run the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', and the AI is 'O'.")
    print_board(board)

    while True:
        # Player's turn
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, e.g., '1 2'): ").split())
                if board[row - 1][col - 1] == " ":
                    board[row - 1][col - 1] = "X"
                    break
                else:
                    print("That spot is already taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers from 1 to 3.")

        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You won!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        # AI's turn
        print("AI is thinking...")
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
            print(f"AI chose row {move[0] + 1}, column {move[1] + 1}.")

        print_board(board)

        if check_winner(board, "O"):
            print("The AI won! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
import random

class Game:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def display_board(self, numbers=None):
        show_numbers_x = numbers in ('x', 'both')
        show_numbers_y = numbers in ('y', 'both')

        print()
        for row_count, row in enumerate(self.board):
            if row_count != 0:
                print("   " + "-" * 9)

            # Row label
            if show_numbers_x:
                print(f"{row_count + 1}  ", end="")
            else:
                print("   ", end="")

            # Columns
            for col_count, col in enumerate(row):
                cell = col if col is not None else ' '
                print(cell, end="")
                if col_count != 2:
                    print(" | ", end="")
            print()

        # Column numbers at bottom
        if show_numbers_y:
            print("\n    1   2   3\n")

    def place_piece(self, piece, x, y):
        self.board[x][y] = piece

def all_equal(lst):
    return lst[0] is not None and lst.count(lst[0]) == len(lst)

def check_win(board):
    # Rows
    for row in board:
        if all_equal(row):
            winner_message(row[0])

    # Columns
    for i in range(3):
        column = [board[0][i], board[1][i], board[2][i]]
        if all_equal(column):
            winner_message(column[0])

    # Diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    for cross in diagonals:
        if all_equal(cross):
            winner_message(cross[0])

def winner_message(piece):
    print(f"\n {piece.upper()} wins! ")
    from sys import exit
    exit()

def ai_move(piece, opponent):
    # Check for winning move
    for x in range(3):
        for y in range(3):
            if game.board[x][y] is None:
                game.board[x][y] = piece
                if is_winner(piece):
                    return x, y
                game.board[x][y] = None

    # Block opponent's winning move
    for x in range(3):
        for y in range(3):
            if game.board[x][y] is None:
                game.board[x][y] = opponent
                if is_winner(opponent):
                    game.board[x][y] = None
                    return x, y
                game.board[x][y] = None

    # Pick random empty spot
    empty = [(x, y) for x in range(3) for y in range(3) if game.board[x][y] is None]
    return random.choice(empty)

def is_winner(piece):
    # Rows
    for row in game.board:
        if all_equal(row) and row[0] == piece:
            return True
    # Columns
    for i in range(3):
        column = [game.board[0][i], game.board[1][i], game.board[2][i]]
        if all_equal(column) and column[0] == piece:
            return True
    # Diagonals
    diagonals = [
        [game.board[0][0], game.board[1][1], game.board[2][2]],
        [game.board[0][2], game.board[1][1], game.board[2][0]]
    ]
    for diag in diagonals:
        if all_equal(diag) and diag[0] == piece:
            return True
    return False

def play(piece, ai=False):
    if ai:
        x, y = ai_move(piece, 'x' if piece == 'o' else 'o')
        game.place_piece(piece, x, y)
        print(f"\nAI ({piece.upper()}) chooses row {x+1}, column {y+1}")
        check_win(game.board)
        game.display_board(numbers='both')
    else:
        print(f"\n{piece.upper()}'s turn.")
        game.display_board(numbers='both')
        try:
            x = int(input("Choose row (1-3): ")) - 1
            y = int(input("Choose column (1-3): ")) - 1
        except ValueError:
            print("Invalid input! Enter numbers 1–3.")
            return play(piece, ai)
        if 0 <= x < 3 and 0 <= y < 3:
            if game.board[x][y] is None:
                game.place_piece(piece, x, y)
                check_win(game.board)
            else:
                print(" Spot already taken. Try again.")
                play(piece, ai)
        else:
            print(" Invalid position. Try again.")
            play(piece, ai)

# --- Main Game ---
game = Game()
turns = 0

while True:
    if turns % 2 == 0:
        play('x')       # Human
    else:
        play('o', ai=True)  # AI
    turns += 1
    if turns == 9:
        game.display_board()
        print("\n It's a draw!")
        break
                
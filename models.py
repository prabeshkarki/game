# model.py
class Game:
    def __init__(self):
        # 3x3 empty board
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        """Display the current game board."""
        print("\n  0   1   2")
        for i, row in enumerate(self.board):
            display_row = [cell if cell is not None else ' ' for cell in row]
            print(f"{i} " + " | ".join(display_row))
            if i < 2:
                print("  " + "-" * 9)

    def make_move(self, row, col):
        """Place the current player's mark at (row, col)."""
        if row not in range(3) or col not in range(3):
            print("Invalid position! Try again.")
            return False
        if self.board[row][col] is not None:
            print("That cell is already taken!")
            return False
        self.board[row][col] = self.current_player
        return True

    def check_winner(self):
        """Return 'X' or 'O' if there is a winner, 'Draw' if tie, or None if still playing."""
        b = self.board
        # Check rows, columns, diagonals
        lines = (
            b[0], b[1], b[2],  # rows
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        )
        for line in lines:
            if line[0] == line[1] == line[2] and line[0] is not None:
                return line[0]

        # Check for draw
        if all(all(cell is not None for cell in row) for row in b):
            return 'Draw'

        return None

    def switch_player(self):
        """Switch turn between players."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

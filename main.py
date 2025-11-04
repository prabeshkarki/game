# main.py
from models import Game

def main():
    print("=== Tic Tac Toe ===")
    game = Game()

    while True:
        game.display_board()
        print(f"\nPlayer {game.current_player}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if not game.make_move(row, col):
            continue  # invalid move, retry

        winner = game.check_winner()
        if winner:
            game.display_board()
            if winner == 'Draw':
                print("\nIt's a draw!")
            else:
                print(f"\nPlayer {winner} wins!")
            break

        game.switch_player()

if __name__ == "__main__":
    main()

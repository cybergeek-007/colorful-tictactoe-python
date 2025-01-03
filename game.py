# game.py
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)


class TicTacToe:
    def __init__(self):
        """Initialize the game board, current player, and game statistics."""
        self.reset_board()
        # Initialize player statistics to track wins and losses
        self.stats = {
            'X': {'wins': 0, 'losses': 0},
            'O': {'wins': 0, 'losses': 0}
        }
        # Define colors for better visual distinction between players and elements
        self.player_colors = {
            'X': Fore.BLUE,
            'O': Fore.RED
        }
        self.number_color = Fore.YELLOW

    def reset_board(self):
        """Reset the game board and current player."""
        # Create a fresh board with numbers 1-9
        self.board = [str(i) for i in range(1, 10)]
        # X always starts first
        self.current_player = 'X'

    def display_stats(self):
        """Display current game statistics for both players."""
        print(f"\n{Fore.CYAN}=== Game Statistics ==={Style.RESET_ALL}")
        for player in ['X', 'O']:
            color = self.player_colors[player]
            print(f"{color}Player {player}:")
            print(f"Wins: {self.stats[player]['wins']}")
            print(f"Losses: {self.stats[player]['losses']}{Style.RESET_ALL}")

    def display_controls(self):
        """Display game controls and options for players."""
        print(f"\n{Fore.CYAN}=== Controls ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}• Enter 1-9 to make a move")
        print(f"• Enter 'n' for new game")
        print(f"• Enter 'q' to quit{Style.RESET_ALL}")

    def update_stats(self, winner):
        """Update player statistics after a game."""
        if winner != 'Draw':
            # Increment winner's wins and loser's losses
            self.stats[winner]['wins'] += 1
            loser = 'O' if winner == 'X' else 'X'
            self.stats[loser]['losses'] += 1

    def get_colored_cell(self, cell):
        """Return a cell value with appropriate coloring."""
        if cell in ['X', 'O']:
            return f"{self.player_colors[cell]}{cell}{Style.RESET_ALL}"
        return f"{self.number_color}{cell}{Style.RESET_ALL}"

    def display_board(self):
        """Display the current game board with colored formatting."""
        print(f"\n{Fore.CYAN}Current Board:{Style.RESET_ALL}")
        for row in range(0, 9, 3):
            # Get colored cells for each row
            cells = [self.get_colored_cell(self.board[i]) for i in range(row, row + 3)]
            print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
            if row < 6:  # Don't print separator after last row
                print(f"{Fore.WHITE}---+---+---{Style.RESET_ALL}")

    def make_move(self, position):
        """Attempt to make a move at the given position."""
        try:
            position = int(position) - 1  # Convert to 0-based index
            if 0 <= position <= 8 and self.board[position].isdigit():
                self.board[position] = self.current_player
                return True
            return False
        except ValueError:
            return False

    def check_winner(self):
        """Check if there's a winner or draw."""
        # Define all possible winning combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        # Check for winner
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                return self.board[combo[0]]

        # Check for draw (no empty cells left)
        if not any(cell.isdigit() for cell in self.board):
            return 'Draw'

        return None

    def switch_player(self):
        """Switch the current player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def save_game_state(self):
        """Save the current game state to a file."""
        with open('game_state.txt', 'w') as file:
            # Save board state row by row
            for row in range(0, 9, 3):
                file.write(','.join(self.board[row:row + 3]) + '\n')
            # Save current player's turn
            file.write(f"Player Turn: {self.current_player}")



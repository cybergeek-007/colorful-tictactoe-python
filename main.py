# main.py
from game import TicTacToe
from colorama import Fore, Style


def display_welcome_message():
    """Display a colorful welcome message and game instructions."""
    print(f"\n{Fore.GREEN}============================")
    print(f"{Fore.GREEN}Welcome to Tic Tac Toe Game!")
    print(f"{Fore.GREEN}============================{Style.RESET_ALL}")
    print(f"\n{Fore.BLUE}Player 1: X{Style.RESET_ALL}")
    print(f"{Fore.RED}Player 2: O{Style.RESET_ALL}")


def get_play_again():
    """Ask if players want to play another game."""
    while True:
        choice = input(f"\n{Fore.GREEN}Would you like to play again? (y/n): {Style.RESET_ALL}").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print(f"{Fore.RED}Please enter 'y' for yes or 'n' for no.{Style.RESET_ALL}")


def main():
    """Main game loop with statistics tracking and enhanced game controls."""
    game = TicTacToe()
    display_welcome_message()

    while True:
        game.display_board()
        game.display_stats()
        game.display_controls()

        # Get player move
        while True:
            player_color = game.player_colors[game.current_player]
            position = input(
                f"\n{player_color}Player {game.current_player}, enter your move (1-9), 'n' for new game, or 'q' to quit: {Style.RESET_ALL}").lower()

            # Handle special commands
            if position == 'q':
                print(f"\n{Fore.YELLOW}Thanks for playing! Final statistics:{Style.RESET_ALL}")
                game.display_stats()
                return
            elif position == 'n':
                print(f"\n{Fore.GREEN}Starting new game...{Style.RESET_ALL}")
                game.reset_board()
                break

            # Handle regular moves
            if game.make_move(position):
                break
            print(f"{Fore.RED}Invalid move! Position already taken or out of range.{Style.RESET_ALL}")

        # Save the game state after each valid move
        game.save_game_state()

        # Check for winner or draw
        result = game.check_winner()
        if result:
            game.display_board()
            if result == 'Draw':
                print(f"\n{Fore.YELLOW}Game Over! It's a draw!{Style.RESET_ALL}")
            else:
                winner_color = game.player_colors[result]
                print(f"\n{winner_color}Game Over! Player {result} wins!{Style.RESET_ALL}")

            # Update and display statistics
            game.update_stats(result)
            game.display_stats()

            # Ask to play again
            if get_play_again():
                game.reset_board()
                print(f"\n{Fore.GREEN}Starting new game...{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.YELLOW}Thanks for playing! Final statistics:{Style.RESET_ALL}")
                game.display_stats()
                break

        game.switch_player()


if __name__ == "__main__":
    main()
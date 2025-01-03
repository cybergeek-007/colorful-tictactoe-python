# Tic Tac Toe Game

Welcome to the Tic Tac Toe game! This is an enhanced version of the classic game featuring a vibrant color-coded interface, statistics tracking, and multiple game control options. The game runs in your console and supports two players taking turns to compete while keeping track of their performance across multiple games.

## Table of Contents
1. [Game Overview](#game-overview)
2. [Installation Guide](#installation-guide)
3. [Game Controls](#game-controls)
4. [How to Play](#how-to-play)
5. [Features](#features)
6. [File Structure](#file-structure)
7. [Troubleshooting](#troubleshooting)

## Game Overview

Our Tic Tac Toe implementation enhances the classic game with modern features:
- Color-coded players and board elements
- Real-time statistics tracking
- Multiple game control options
- Game state saving
- Clear, intuitive interface
- Two-player competitive gameplay

## Installation Guide

### Prerequisites
- Python 3.x installed on your system
- Basic familiarity with command line/terminal

### Step-by-Step Installation

1. **Install Python** (if not already installed):
   - Download Python from [python.org](https://python.org)
   - Make sure to check "Add Python to PATH" during installation

2. **Install Required Package**:
   ```bash
   pip install colorama
   ```

3. **Setup Game Files**:
   - Create a new directory for the game
   - Save the provided code in two files:
     - `game.py`: Contains game logic
     - `main.py`: Contains main game loop

4. **Run the Game**:
   ```bash
   python main.py
   ```

## Game Controls

The game offers multiple control options during gameplay:

### Basic Controls
- **Numbers (1-9)**: Make a move on the corresponding board position
- **'n'**: Start a new game at any time (resets board without affecting statistics)
- **'q'**: Quit the game and display final statistics

### End of Game Options
- **'y'**: Play another game after completion (saves game outcome)
- **'n'**: End the session and display final statistics

Board Position Numbers:
```
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
```

## How to Play

1. **Starting the Game**:
   - Run the game using `python main.py`
   - The board will be displayed with numbered positions
   - Player X (Blue) starts first

2. **Making Moves**:
   - Enter a number (1-9) to place your mark
   - The board updates after each valid move
   - Invalid moves will be rejected with an error message

3. **During Gameplay**:
   - Current player is shown in their color (Blue/Red)
   - Available positions are shown in yellow
   - You can start a new game anytime with 'n'
   - Quit anytime with 'q'

4. **Game End**:
   - Winner or draw is announced
   - Statistics are updated and displayed
   - Option to play again or end session

## Features

### Color Coding
- Player X: Blue
- Player O: Red
- Available Positions: Yellow
- Grid Lines: White
- Messages: Various colors for different types of information

### Statistics Tracking
- Wins and losses recorded for both players
- Statistics displayed after each move
- Statistics maintained across multiple games in a session
- Final statistics shown when quitting

### Game Control Options
1. **Mid-Game Controls**:
   - Start new game ('n'): Resets board without recording outcome
   - Quit game ('q'): Ends session with final statistics
   - Regular moves (1-9): Place mark on board

2. **Post-Game Options**:
   - Play again: Starts new game after recording outcome
   - End session: Shows final statistics and exits

### Auto-Save Functionality
- Game state saved after each move
- Includes board position and current player
- Stored in 'game_state.txt'

## File Structure
```
tic-tac-toe/
├── main.py           # Game entry point and main loop
├── game.py           # Game logic and TicTacToe class
├── game_state.txt    # Auto-generated save file (created during play)
└── README.md         # This documentation
```

## Troubleshooting

### Common Issues and Solutions

1. **Colors Not Displaying**:
   - Ensure colorama is installed correctly
   - Try reinstalling: `pip install --upgrade colorama`
   - Check terminal color support

2. **Invalid Move Messages**:
   - Use only numbers 1-9 for moves
   - Ensure position isn't already taken
   - Don't use spaces or special characters

3. **Game Not Starting**:
   - Verify Python installation
   - Check both files are in same directory
   - Ensure correct file names: `game.py` and `main.py`

4. **Statistics Issues**:
   - Use 'q' to quit properly (don't close window)
   - Complete games for proper stat recording
   - Use 'n' for new game without recording stats

---

For support or questions, please report issues on the GitHub repository.

Enjoy playing! 🎮

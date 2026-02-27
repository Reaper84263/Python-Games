# Overview

This is a collection of classic console-based games written in Python, including Hangman and Three Card Monte. The project demonstrates fundamental programming concepts like input validation, game logic, and user interaction through a command-line interface. The codebase appears to be part of a programming course assignment, focusing on function-based design and proper code organization.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Design Pattern
The project follows a modular, function-based architecture with clear separation of concerns:

- **Input Validation Module**: A dedicated `check_input.py` module provides reusable input validation functions for integers, ranges, and yes/no responses
- **Game Logic Separation**: Each game implements its core logic in separate functions that handle specific responsibilities (display, user input, game state)
- **Data Separation**: Game data (word dictionary) is stored in separate modules for easy maintenance

## Game Implementation Strategy
Each game follows a consistent pattern:
1. Main game loop with user choice to continue/quit
2. Game-specific helper functions for display and logic
3. Input validation using the shared check_input module
4. Clear separation between game state management and user interface

## Input Validation Architecture
The `check_input` module provides a centralized approach to input validation:
- Exception handling for type conversion errors
- Range validation for bounded inputs
- Reusable validation functions that can be imported by any game

## Game State Management
Games maintain state through simple data structures:
- Lists for tracking guessed letters, incorrect guesses
- Counters for game progression
- Boolean flags for game completion conditions

# External Dependencies

## Built-in Python Modules
- **random**: Used for selecting random words from the dictionary and generating random card positions
- **Standard I/O**: All user interaction handled through built-in `input()` and `print()` functions

## Internal Dependencies
- **dictionary.py**: Contains word list for Hangman game
- **check_input.py**: Shared input validation utilities used across games

## No External Libraries
The project is designed to run with only Python's standard library, making it highly portable and suitable for educational environments without additional package management requirements.
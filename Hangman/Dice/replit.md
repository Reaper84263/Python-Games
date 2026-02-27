# Overview

This is a Python-based dice game where a player rolls 5 dice and scores points based on specific patterns (three of a kind, series of 3 consecutive numbers, or a pair). The game allows repeated turns until the player chooses to quit, tracking cumulative score throughout the session.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Application Structure
The application follows an object-oriented design with clear separation of concerns:

- **Die Class** (`die.py`) - Represents individual dice with configurable sides (default 6). Implements comparison operators (`__lt__`, `__eq__`, `__sub__`) to enable sorting and comparison of dice values. Uses Python's `random` module for dice rolling.

- **Player Class** (`player.py`) - Manages player state including name, collection of 5 dice, and cumulative score. Handles game logic for detecting scoring patterns (pair, three of a kind, series). Dice are automatically sorted after each roll to simplify pattern detection.

- **Main Game Loop** (`main.py`) - Orchestrates game flow with turn-based gameplay. Each turn involves rolling dice, displaying results, checking for scoring patterns, and updating score. The game continues until player opts out.

- **Input Validation Module** (`check_input.py`) - Provides reusable input validation functions. Currently implements `get_int()` with error handling for integer input. Contains placeholder for `get_positive_int()` (incomplete). References `get_yes_no()` function in main.py but implementation is missing from the module.

## Design Patterns
- **Object-Oriented Design**: Encapsulation of dice and player logic into separate classes
- **Operator Overloading**: Die class implements comparison operators for intuitive dice comparison
- **Separation of Concerns**: Input validation separated into dedicated module for reusability

## Scoring System
Points are awarded cumulatively:
- Three of a kind: +3 points
- Series (3 consecutive numbers): +2 points  
- Pair (2 matching dice): +1 point
- Priority order: Three of a kind checked first, then series, then pair (only one pattern scores per turn)

# External Dependencies

## Standard Library Dependencies
- **random** - Used for generating random dice values (1 to number of sides)

## Missing Implementations
- `check_input.get_yes_no()` - Referenced in main.py but not implemented in check_input.py
- `check_input.get_positive_int()` - Partially implemented but incomplete (missing validation loop and return logic)

No external third-party packages, databases, or APIs are used in this application.
# Overview

This is a console-based racing game called "Rad Racer" built in Python. Players select one of three vehicle types (Car, Motorcycle, or Truck) and race against AI opponents on a 3-lane track with obstacles. Each vehicle has unique abilities and characteristics, utilizing object-oriented programming with abstract base classes and polymorphism.

The game features:
- 3-lane track of 100 cells with randomly placed obstacles
- Turn-based movement with three move types: slow (safe), fast (energy-consuming), and special (unique per vehicle)
- Energy management system (100 starting energy)
- AI opponents with probabilistic decision-making
- Vehicle-specific special moves with different risk/reward profiles

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Object-Oriented Design Pattern

**Problem**: Need to model different vehicle types with shared behavior but unique special abilities.

**Solution**: Abstract base class inheritance hierarchy with polymorphism.

**Architecture**:
- `Vehicle` (abstract base class) - Defines common attributes (position, energy, speed, name, initial) and shared methods (fast, slow movement)
- `Car` - Implements Nitro Boost special (1.5x speed with randomness, crashes on obstacles)
- `Motorcycle` - Implements Wheelie special (2x speed with 75% success rate) and enhanced slow movement (75% speed instead of 50%)
- `Truck` - Implements Ram special (2x speed, ignores obstacles)

**Rationale**: This allows code reuse for common racing mechanics while enabling unique special moves through method overriding. The abstract base ensures all vehicles implement required methods.

## Game State Management

**Problem**: Need to track multiple vehicles across lanes with obstacles and enforce racing rules.

**Solution**: Procedural game loop with centralized state tracking in main.py.

**Architecture**:
- Track represented as 3 lanes × 100 positions
- Obstacles stored as positions per lane
- Vehicle instances maintain their own position and energy
- Main loop orchestrates turns, move validation, and collision detection

**Rationale**: Simple state management appropriate for a turn-based console game. Centralized control in main.py makes game flow easy to follow.

## Movement and Energy System

**Problem**: Balance different movement strategies with risk/reward mechanics.

**Solution**: Three-tier movement system with energy costs:
- **Slow move**: 50% speed (75% for Motorcycle), free, avoids obstacles
- **Fast move**: Full speed ±1, costs 5 energy, crashes on obstacles
- **Special move**: Vehicle-specific ability, costs 15 energy, unique mechanics per class

**Rationale**: Creates strategic depth where players must balance speed, energy management, and risk. Each vehicle offers different trade-offs.

## Collision Detection

**Problem**: Determine when vehicles hit obstacles and apply appropriate consequences.

**Solution**: Position-based collision checking with move-type dependent behavior:
- Slow moves: automatically go around obstacles
- Fast/Special moves: crash and stop at obstacle (except Truck Ram)
- Collision logic embedded in each move method

**Rationale**: Encapsulating collision logic within move methods keeps the code modular and allows vehicle-specific override behavior (e.g., Truck ignoring obstacles).

## AI Opponent Behavior

**Problem**: Create believable computer-controlled racers.

**Solution**: Probability-based decision making:
- 40% slow move
- 30% fast move
- 30% special move
- Fallback to safe moves when energy insufficient

**Rationale**: Fixed probabilities create consistent but varied AI behavior without complex decision trees. Energy constraints add realistic limitations.

## Input Validation

**Problem**: Ensure robust user input handling.

**Solution**: Dedicated `check_input` module with validation functions for integers, ranges, and yes/no responses.

**Architecture**:
- `get_int()` - validates integer input
- `get_positive_int()` - validates non-negative integers
- `get_int_range()` - validates integers within bounds

**Rationale**: Centralized validation logic prevents crashes from invalid input and can be reused across different input scenarios.

## Randomness and Variability

**Problem**: Prevent deterministic, repetitive gameplay.

**Solution**: Random elements throughout:
- Obstacle placement (2 per lane, random positions)
- Movement variance (±1 for most moves)
- Special move outcomes (Motorcycle wheelie 75% success)
- AI move selection

**Rationale**: Randomness increases replayability and prevents players from memorizing optimal strategies.

# External Dependencies

## Standard Library Modules

- **random** - Used for movement variance, obstacle placement, AI decision-making, and special move success rates
- **math** - Used for floor operations in speed calculations (especially for fractional speed multipliers like 1.5x and 0.75x)
- **typing** - Provides type hints (Optional, List, Tuple) for better code documentation and IDE support
- **abc** - Provides abstract base class functionality (abstractmethod decorator) for the Vehicle class hierarchy

**Note**: This is a standalone Python application with no external package dependencies, databases, or API integrations. All functionality is implemented using Python's standard library.
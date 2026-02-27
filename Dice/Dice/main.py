from die import Die
from player import Player
import check_input

def take_turn(player):
    player.roll_dice()
    print(player)
    if player.has_three__of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_series():
        print("You got a series of 3!")
    elif player.has_pair():
        print("You got a pair!")
    else:
        print("Aww. Too bad.")

    print(f"Score = {player.points()}")

def main():
  player = Player("Player 1")
  take_turn(player)
  while True:
    #take_turn(player)
    choice = input("Play again? (Y/N): ").strip().lower().upper()
    #choice = check_input.get_yes_no("Play again? (Y/N): ")
    
    
    if choice == "Y":
      take_turn(player)
      
      
    elif choice == "N":
      print("Game over!")
      print(f"Final score = {player.points()}")
      break
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
  main()

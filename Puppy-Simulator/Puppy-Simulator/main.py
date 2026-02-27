from puppy import Puppy
import check_input

def main():
   puppy = Puppy()
   print("Congratulations on your new puppy!")

   choice = 0
   while choice != 3:
      print("What would you like to do?")
      print("1. Feed the puppy")
      print("2. Play with the puppy")
      print("3. Quit")
      choice = check_input.get_int_range("Enter choice: ", 1, 3)

      if choice == 1:
        reaction = puppy.give_food()
        print(reaction)
      elif choice == 2:
        reaction = puppy.throw_ball()
        print(reaction)

if __name__ == "__main__":
   main()
         
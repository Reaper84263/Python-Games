from puppy_state import PuppyState
from state_asleep import StateAsleep

class StatePlay(PuppyState):
   def feed(self, puppy):
      return ("The puppy is too busy playing with the ball to eat right now.")

   def play(self, puppy):
      puppy.inc_plays()
      if puppy.plays < 3:
         return ("You throw the ball again and the puppy excitedly chases it.")
      else:
         message = ("You throw the ball again and the puppy excitedly chases it. " + "\n" + "The puppy played so much it fell asleep!")
         puppy.change_state(StateAsleep())
         return message
from state_play import StatePlay
from puppy_state import PuppyState
from state_asleep import StateAsleep
class StateEat(PuppyState):
   def feed(self, puppy):
      puppy.inc_feeds()

      if puppy.feeds < 3:
         return "The puppy continues to eat as you add another scoop of kibble to its bowl."
      else:
         message = "The puppy continues to eat as you add another scoop of kibble to its bowl." + "\n" + "The puppy ate so much it fell asleep!"
         puppy.change_state(StateAsleep())
         return message

   def play(self, puppy):
      puppy.change_state(StatePlay())
      puppy.inc_plays()
      return "The puppy looks up from its food and chases the ball you threw."
     
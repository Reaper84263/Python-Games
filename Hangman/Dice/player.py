from die import Die

class Player:

  def __init__(self, name):
      self.name = name
      self.dice = [Die() for _ in range(3)]
      self.score = 0

  def points(self):
      return self.score

  def roll_dice(self):
      for die in self.dice:
          die.roll()
      self.dice.sort()
        

  def has_pair(self):
      for i in range(len(self.dice)-1):
          if self.dice[i] == self.dice[i+1]:
              self.score += 1
              return True
      return False

  def has_three__of_a_kind(self):
      for i in range(len(self.dice) - 2):
          if self.dice[i] == self.dice[i+1] == self.dice[i+2]:
              self.score += 3
              return True
      return False

  def has_series(self):
      for i in range(len(self.dice) - 2):
          if self.dice[i].value + 1 == self.dice[i+1].value and self.dice[i+1].value + 1 == self.dice[i+2].value:
              self.score += 2
              return True
      return False

  def __str__(self):
      dice_str = ", ".join([f"D{i+1}={self.dice[i]}" for i in range(len(self.dice))])
      return dice_str

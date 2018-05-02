from PyQt5.QtCore import QByteArray

from Mobile import Mobile


class Ship(Mobile):
   """This is what the user controls"""
   #
   # Maybe add player class?
   #
   def __init__(self, lives=3):
       """ Inherits __init__ from Mobile class. Always starts with 3 lives instead of 1."""
       self.lives = lives
       super().__init__(self)

   def lose_life(self):
       """Removes one life to ship lives"""
       self.lives -= 1
       return self.lives

   def gain_life(self):
       """Adds one life to ship lives"""
       self.lives += 1
       return self.lives

   def move(self, direction, pixels):
       """Moves ship on screen and resets ship location"""
       if direction == 'left':
           self.x -= pixels
       elif direction == 'right':
           self.x += pixels
       elif direction == 'forward':
           self.y += pixels
       elif direction == 'back':
           self.y -= pixels
       return self.loc

from PyQt5.QtCore import QByteArray


from Mobile import Mobile


class Ship(Mobile):
   """This is what the user controls"""
   #
   # Maybe add player class?
   #
   def __init__(self, image, height, width, x, y, lives=3):
       """ Inherits __init__ from Mobile class. Always starts with 3 lives instead of 1."""
       super().__init__(image, height, width, x, y, lives=3)

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
       self.loc = [self.x, self.y]
       return self.loc

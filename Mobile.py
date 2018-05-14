class Mobile(object):
   """This class is what Ship and Obstacle will inherit from"""
   #
   # Image is the image file(png, jpeg, jpg,etc.) used for the object
   # size is the collision area for the object
   # Location is where it is on the screen
   #
   def __init__(self, image, height, width, x, y, lives=1):
       self.image = image
       self.x = x
       self.y = y
       #
       # edit to be colored pixels in png, not whole box
       #
       self.height = height
       self.width = width
       self.loc = [self.x, self.y]
       self.lives = lives
       self.box = None

   def change_image(self, image):
       """Changes image is the image file(png, jpeg, jpg,etc.) used for the object"""
       self.image = image
       return self.image

   def change_size(self, height, width):
       """changes size is the collision area for the object"""
       self.height = height
       self.width = width
       return self.height, self.width

   def lose_life(self):
       """Removes one life to ship lives"""
       self.lives -= 1

   def gain_life(self):
       """Adds one life to ship lives"""
       self.lives += 1
       return self.lives

   def move(self, pixels):
       """Moves ship on screen and resets ship location"""
       #
       # Object forwards moves it down on screen towards player, so self.y -= 1 instead of self.y += 1.
       #
       self.y += pixels
       self.loc = [self.x, self.y]
       return self.loc

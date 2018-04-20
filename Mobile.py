class Mobile(object):
    """This class is what Ship and Obstacle will inherit from"""
    #
    # Image is the image file(png, jpeg, jpg,etc.) used for the object
    # size is the collision area for the object
    # Location is where it is on the screen
    #
    def __init__(self, image, size, location, lives=3):
        self.image = image
        self.size = size
        self.loc = location
        self.lives = 3

    def move(self):
        pass
    #
    # I'm not even sure we need a move here, but in case
    #

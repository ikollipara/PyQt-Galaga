from PyQt5.QtCore.QByteArray import size

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

    def move(self, dir, dx):
        """Moves ship on screen and resets ship location"""
        if dir == 'left':
            self.x -= dx
        elif dir == 'right':
            self.x += dx
        elif dir == 'forward':
            self.y += dx
        elif dir == 'back':
            self.y -= dx
        return self.loc

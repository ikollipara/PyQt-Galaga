from Mobile import Mobile

class Bullet(Mobile):
    def __init__(self, image, height, width, x, y, lives=1):
        super().__init__(image, height, width, x, y, lives=1)
        self.box = None

    def move(self, pixels):
        """Moves bullet on screen up toward obstacles"""
        #
        # Object forwards moves it up on screen towards obstacles, so self.y -= 1 instead of self.y += 1.
        #
        self.y -= pixels
        self.loc = [self.x, self.y]
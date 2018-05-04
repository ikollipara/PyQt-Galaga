class World(object):
    def __init__(self, xSize=1000, ySize=900):
        self.xSize = xSize
        self.ySize = ySize
        self.objLocations = []

    def update_positions(self, location, height, width):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        bottomleft = ((location[0]-(width/2)), (location[1]-(height/2)))
        topRight = ((location[0]+(width/2)), (location[1]+(height/2)))
        objLocation = (bottomleft, topRight)
        self.objLocations.append(objLocation)

    def detect_collision(self):
        pass

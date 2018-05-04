class World(object):
    def __init__(self, xSize=1000, ySize=900):
        self.xSize = xSize
        self.ySize = ySize
        self.objLocations = []

    def update_positions(self, location, height, width):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        coordinates = []
        # bottomleft = ((location[0]-(width/2)), (location[1]-(height/2)))
        # topRight = ((location[0]+(width/2)), (location[1]+(height/2)))
        # objLocation = (bottomleft, topRight)
        # self.objLocations.append(objLocation)
        bottomleft = (int(location[0] - (width / 2)), int(location[1] - (height / 2)))
        topRight = (int(location[0] + (width / 2)), int(location[1] + (height / 2)))
        coordinates.append(bottomleft)
        coordinates.append(topRight)
        # for number in range(0, width + 1):
        #     coordinate = ((bottomleft[0] + number), (bottomleft[1]))
        #     coordinates.append(coordinate)
        # for number in range(0, height + 1):
        #     coordinate = ((topRight[0]), (topRight[1] + number))
        #     coordinates.append(coordinate)
        for coordinate in coordinates:
            print(coordinate)

    def detect_collision(self):
        pass

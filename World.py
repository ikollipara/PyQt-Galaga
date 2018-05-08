class World(object):
    def __init__(self, xSize=1000, ySize=900):
        self.xSize = xSize
        self.ySize = ySize
        self.obstacleLocations = []
        self.shipLocations = None

    def update_obstacle_position(self, location, height, width):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        bottomleft = (int(location[0] - (width / 2)), int(location[1] - (height / 2)))
        topRight = (int(location[0] + (width / 2)), int(location[1] + (height / 2)))
        locations = [bottomleft, topRight]
        self.obstacleLocations.append(locations)

    def update_ship_position(self, location, height, width):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        bottomleft = (int(location[0] - (width / 2)), int(location[1] - (height / 2)))
        topRight = (int(location[0] + (width / 2)), int(location[1] + (height / 2)))
        self.shipLocations = [bottomleft, topRight]

    def detect_collision(self):
        collided = False
        for obstacleLocation in self.obstacleLocations:
            bottomLeftX = obstacleLocation[0][0]
            bottomLeftY = obstacleLocation[0][1]
            if bottomLeftX >= self.shipLocations[0][0] and bottomLeftX <= self.shipLocations[1][0]:
                if bottomLeftY >= self.shipLocations[1][1] and bottomLeftY <= self.shipLocations[0][1]:
                    collided = True
                    print("OOOOOOOOOOOOOO")
        # return collided




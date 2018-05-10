class World(object):
    def __init__(self, controller, xSize=1000, ySize=900):
        self.xSize = xSize
        self.ySize = ySize
        self.obstacleLocations = []
        self.shipLocations = None
        self.controller = controller

    def update_obstacle_positions(self):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        self.obstacleLocations = []
        for obstacle in self.controller.obstacles:
            bottomleft = (int(obstacle.loc[0] - (obstacle.width / 2)), int(obstacle.loc[1] + (obstacle.height / 2)))
            topRight = (int(obstacle.loc[0] + (obstacle.width / 2)), int(obstacle.loc[1] - (obstacle.height / 2)))
            locations = [bottomleft, topRight]
            self.obstacleLocations.append(locations)

    def update_ship_position(self, location, height, width):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        bottomleft = (int(location[0] - (width / 2)), int(location[1] + (height / 2)))
        topRight = (int(location[0] + (width / 2)), int(location[1] - (height / 2)))
        self.shipLocations = [bottomleft, topRight]

    def detect_collision(self):
        collided = False
        for obstacleLocation in self.obstacleLocations:
            bottomLeftX = obstacleLocation[0][0]
            bottomLeftY = obstacleLocation[0][1]
            if type(self.shipLocations) == type([]):
                if bottomLeftX >= self.shipLocations[0][0] and bottomLeftX <= self.shipLocations[1][0]:
                    print("X")
                    if bottomLeftY >= self.shipLocations[1][1] and bottomLeftY <= self.shipLocations[0][1]:
                        collided = True
                        print("OOOOOOOOOOOOOO")
        return collided




class World(object):
    def __init__(self, controller, xSize=1000, ySize=900):
        self.xSize = xSize
        self.ySize = ySize
        self.controller = controller

    def update_obstacle_positions(self, obs):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        # self.obstacleLocations = []
        # for obstacle in self.controller.obstacles:
        #     bottomleft = (int(obstacle.loc[0] - (obstacle.width / 2)), int(obstacle.loc[1] + (obstacle.height / 2)))
        #     topRight = (int(obstacle.loc[0] + (obstacle.width / 2)), int(obstacle.loc[1] - (obstacle.height / 2)))
        #     locations = (bottomleft, topRight)
        #     self.obstacleLocations.append(locations)
        topLeft = obs.loc
        bottomRight = [obs.loc[0]+obs.width, obs.loc[1]+obs.height]
        obs.box = [topLeft, bottomRight]

    def update_ship_position(self):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        # bottomleft = (int(location[0] - (width / 2)), int(location[1] + (height / 2)))
        # topRight = (int(location[0] + (width / 2)), int(location[1] - (height / 2)))
        # self.shipLocations = [bottomleft, topRight]
        topLeft = self.controller.ship.loc
        bottomRight = [self.controller.ship.loc[0]+self.controller.ship.width, self.controller.ship.loc[1]+self.controller.ship.height]
        self.controller.ship.box = [topLeft, bottomRight]

    def detect_collision(self):
        collided = False
        collision = 0
        # for obstacleLocation in self.obstacleLocations:
        #     bottomLeftX = obstacleLocation[0][0]
        #     bottomLeftY = obstacleLocation[0][1]
        #     topRightX = obstacleLocation[1][0]
        #     topRightY = obstacleLocation[0][1]
        #     if type(self.shipLocations) == type([]):
        #         if bottomLeftX >= self.shipLocations[0][0] and bottomLeftX <= self.shipLocations[1][0]:
        #             print("X")
        #             if bottomLeftY >= self.shipLocations[1][1] and bottomLeftY <= self.shipLocations[0][1]:
        #                 collided = True
        #             if topRightY >= self.shipLocations[1][1] and topRightY <= self.shipLocations[0][1]:
        #                 collided = True
        #         if topRightX >= self.shipLocations[0][0] and topRightX <= self.shipLocations[1][0]:
        #             print("Y")
        #             if bottomLeftY >= self.shipLocations[1][1] and bottomLeftY <= self.shipLocations[0][1]:
        #                 collided = True
        #             if topRightY >= self.shipLocations[1][1] and topRightY <= self.shipLocations[0][1]:
        #                 collided = True
        #     if collided == True:
        #         print("\nOOOOOOOOOO\n")
        if self.controller.ship.box == None:
            pass
        else:
            shipBox = self.create_collision_box(self.controller.ship.box)
            for obs in self.controller.obstacles:
                obsBox = self.create_collision_box(obs.box)
                for pixel in obsBox[0]:
                    if pixel in shipBox[0]:
                        if collision == 0:
                            collision += 1
                        else: pass
                for pixel in obsBox[1]:
                    if pixel in shipBox[1]:
                        if collision == 1:
                            collision += 1
                        else: pass
                if collision == 2:
                    collided = True
                    print(collided)
        return collided

    def create_collision_box(self, boxList):
        topLeft = boxList[0]
        topRight = [boxList[1][0], boxList[0][1]]
        bottomLeft = [boxList[0][0], boxList[1][1]]
        bottomRight = boxList[1]
        top = list(range(topLeft[0], topRight[0]+1))
        left = list(range(topLeft[1], bottomLeft[1]+1))
        box = [top, left]
        return box




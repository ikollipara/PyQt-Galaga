class World(object):
    def __init__(self, controller, xSize=1000, ySize=900):
        self.xSize = xSize
        self.ySize = ySize
        self.controller = controller

    def update_obstacle_positions(self, obs):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        topLeft = obs.loc
        bottomRight = [obs.loc[0]+obs.width, obs.loc[1]+obs.height]
        obs.box = [topLeft, bottomRight]

    def update_ship_position(self):
        """Finds the top right and bottom left coordinates or the object and appends them"""
        topLeft = self.controller.ship.loc
        bottomRight = [self.controller.ship.loc[0]+self.controller.ship.width, self.controller.ship.loc[1]+self.controller.ship.height]
        self.controller.ship.box = [topLeft, bottomRight]

    def update_bullet_position(self, bullet):
        topLeft = bullet.loc
        bottomRight = [bullet.loc[0] + bullet.width, bullet.loc[1] + bullet.height]
        bullet.box = [topLeft, bottomRight]

    def detect_ship_collision(self):
        if self.controller.ship.box == None:
            pass
        else:
            shipBox = self.create_collision_box(self.controller.ship.box)
            for obs in self.controller.obstacles:
                collision = 0
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
                    self.controller.remove_obstacle(obs)
                    self.controller.ship.lose_life()

    def detect_bullet_collision(self):
        for bullet in self.controller.ship.bullets:
            bulletBox = self.create_collision_box(bullet.box)
            for obs in self.controller.obstacles:
                collision = 0
                obsBox = self.create_collision_box(obs.box)
                for pixel in obsBox[0]:
                    if pixel in bulletBox[0]:
                        if collision == 0:
                            collision += 1
                        else: pass
                for pixel in obsBox[1]:
                    if pixel in bulletBox[1]:
                        if collision == 1:
                            collision += 1
                        else: pass
                if collision == 2:
                    self.controller.remove_obstacle(obs)
                    self.controller.ship.bullets.remove(bullet)

    def create_collision_box(self, boxList):
        topLeft = boxList[0]
        topRight = [boxList[1][0], boxList[0][1]]
        bottomLeft = [boxList[0][0], boxList[1][1]]
        bottomRight = boxList[1]
        top = list(range(topLeft[0], topRight[0]+1))
        left = list(range(topLeft[1], bottomLeft[1]+1))
        box = [top, left]
        return box




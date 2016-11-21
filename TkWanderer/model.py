from random import randint

# **********************Map************************
class Map():
    def __init__(self):
        self.tile_position = [[0, 0, 0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                              [0, 0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                              [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                              [0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]
        self.map_size = [720, 792]
        self.number_of_monsters = randint(1, 3)

# *******************Characters********************

class Character():

    def __init__(self, tile_position):
        self.position = self.randomize_position(tile_position)

    def randomize_position(self, tile_position):
        x, y = randint(0, 9), randint(0, 10)
        print(x,y)
        if tile_position[y][x] == 1:
            print('wall ')
            return self.randomize_position(tile_position)
        return x, y

class Hero(Character):
    pass

class Monster(Character):

    def __init__(self):
        pass

class Boss(Monster):

    def __init__(self):
        pass

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
        self.number_of_monsters = randint(1, 3)
        self.map_size = [10, 11]

# *******************Characters********************

class Character():

    def __init__(self, tile_position):
        self.position = self.randomize_position(tile_position)
        print(self.position)
        self.stats = [100, 100, 50, 50]

    def randomize_position(self, tile_position):
        x, y = randint(0, 9), randint(0, 10)
        print(x,y)
        if tile_position[y][x] == 1:
            print('wall ')
            return self.randomize_position(tile_position)
        return x, y

    def move(self, direction, tile_position):
        new_position = [self.position[0]+direction[0], self.position[1]+direction[1]]
        if self.is_valid_move(new_position, tile_position):
            return new_position
        else:
            return self.position

    def is_valid_move(self, new_position, tile_position):
        inside_map = new_position[0] >= 0 and new_position[0] <= 9 and new_position[1] >= 0 and new_position[1] <= 10
        return tile_position[new_position[1]][new_position[0]] == 0 and inside_map

class Hero(Character):

    pass


class Monster(Character):

    pass

class Boss(Monster):

    pass

# *********************Events**********************
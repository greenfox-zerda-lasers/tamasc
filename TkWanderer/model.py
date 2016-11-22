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
        self.number_of_skeletons = randint(3, 5)
        self.map_size = [10, 11]

# *******************Characters********************

class Character():

    def __init__(self, tile_position):
        self.position = self.randomize_position(tile_position)
        self.stats = [100, 100, 50, 50]

    def randomize_position(self, tile_position):
        x, y = randint(0, 9), randint(0, 10)
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
        try:
            return tile_position[new_position[1]][new_position[0]] == 0 and inside_map
        except IndexError:
            return False


class Hero(Character):

    pass


class Skeleton(Character):

    pass

class Boss(Character):

    pass

# *********************Events**********************

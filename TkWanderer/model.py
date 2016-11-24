from random import randint

# **********************Map************************
class Map():
    def __init__(self):
        self.wall_position = [[0, 0, 0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                              [0, 0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                              [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 0]]
        self.occupied_tile_position = self.wall_position[:]
        self.number_of_skeletons = randint(3, 5)
        self.map_size = [len(self.wall_position[0]), len(self.wall_position)]

# *******************Characters********************

class Character():

    def __init__(self, occupied_tile_position):
        self.position = self.randomize_position(occupied_tile_position)
        self.has_key = False

    def randomize_position(self, occupied_tile_position):
        x, y = randint(0, 9), randint(0, 9)
        if occupied_tile_position[y][x] == 1:
            return self.randomize_position(occupied_tile_position)
        occupied_tile_position[y][x] = 1
        return x, y

    def move(self, direction, occupied_tile_position):
        new_position = [self.position[0]+direction[0], self.position[1]+direction[1]]
        if self.is_valid_move(new_position, occupied_tile_position):
            occupied_tile_position[self.position[1]][self.position[0]] = 0
            occupied_tile_position[new_position[1]][new_position[0]] = 1
            return new_position, occupied_tile_position
        else:
            return self.position, occupied_tile_position

    def is_valid_move(self, new_position, wall_position):
        inside_map = new_position[0] >= 0 and new_position[
            0] <= 9 and new_position[1] >= 0 and new_position[1] <= 10
        try:
            return wall_position[new_position[1]][new_position[0]] == 0 and inside_map
        except IndexError:
            return False


class Hero(Character):

    def __init__(self, occupied_tile_position):
        super().__init__(occupied_tile_position)
        self.level = 1
        self.stats = [20 + 2*randint(1, 6), 2*randint(1, 6), 5 + randint(1, 6)]   #HP DP SP
        self.current_HP = self.stats[0]
        self.has_killed_boss = False

    def level_up(self):
        self.level += 1
        self.stats = [stats + randint(1,6) for stats in self.stats]


class Skeleton(Character):

    def __init__(self, occupied_tile_position, level):
        super().__init__(occupied_tile_position)
        self.stats = [2*level*randint(1, 6) + randint(1, 6), level/2*randint(
            1, 6) + randint(1, 6)/2, level*randint(1, 6) + level]   #HP DP SP
        self.current_HP = self.stats[0]

class Boss(Character):

    def __init__(self, occupied_tile_position, level):
        super().__init__(occupied_tile_position)
        self.level = 1
        self.stats = [2*level*randint(1, 6) + randint(1, 6), level/2*randint(
            1, 6) + randint(1, 6)/2, level*randint(1, 6) + level]   #HP DP SP
        self.current_HP = self.stats[0]

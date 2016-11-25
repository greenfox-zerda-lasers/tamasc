from random import randint

# **********************Map************************
class Map():
    def __init__(self):
        self.map_size = [10, 10]
        self.wall_position = self.randomize_map()
        self.occupied_tile_position = self.wall_position[:]
        self.number_of_skeletons = randint(3, 5)

    def next_level_map(self):
        self.wall_position = self.randomize_map()
        self.occupied_tile_position = self.wall_position[:]

    def randomize_map(self):
        occupied_tile_position = []
        for i in range(self.map_size[1]):
            x = []
            for j in range(self.map_size[0]):
                if randint(0, 100) < 18:
                    x.append(1)
                else:
                    x.append(0)
            occupied_tile_position.append(x)
        return occupied_tile_position
    #

# *******************Characters********************
class Character():

    def __init__(self, occupied_tile_position):
        self.moves = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}
        self.position = self.randomize_position(occupied_tile_position)
        self.has_key = False

    def randomize_position(self, occupied_tile_position):
        x, y = randint(0, 9), randint(0, 9)
        valid_move_list = []
        for direction in self.moves.values():
            new_position = [x+direction[0], y+direction[1]]
            valid_move_list.append(self.is_valid_move(new_position, occupied_tile_position))
        if occupied_tile_position[y][x] == 1 or True not in valid_move_list:
            return self.randomize_position(occupied_tile_position)
        occupied_tile_position[y][x] = 1
        return [x, y]

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
        self.stats = [ 2*randint(1, 6), 2*randint(1, 6), 5 + randint(1, 6)]   #HP DP SP
        self.current_HP = self.stats[0]
        self.has_killed_boss = False
        self.isDead = False

    def level_up(self):
        self.level += 1
        self.stats = [stats + randint(1,6) for stats in self.stats]

    def restore_health(self):
        chance = randint(1, 10)
        if chance > 5:
            self.current_HP = min(self.stats[0], self.current_HP + self.current_HP*0.1)
        elif chance < 2:
            self.current_HP = self.stats[0]
        else:
            self.current_HP = min(self.stats[0], self.current_HP + self.current_HP/3)


class Skeleton(Character):

    def __init__(self, occupied_tile_position, level):
        super().__init__(occupied_tile_position)
        self.stats = [2.5*level*randint(1, 6) + randint(1, 6), level/1.5*randint(
            1, 6) + randint(1, 6)/1.5, level*randint(1, 6) + 1.5*level]   #HP DP SP
        self.current_HP = self.stats[0]


class Boss(Character):

    def __init__(self, occupied_tile_position, level):
        super().__init__(occupied_tile_position)
        self.level = 1
        self.stats = [3*level*randint(1, 6) + randint(1, 6), level*randint(
            1, 6) + randint(1, 6)/2, level*randint(1, 6) + 2*level]   #HP DP SP
        self.current_HP = self.stats[0]

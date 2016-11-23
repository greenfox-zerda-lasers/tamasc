from model import Map, Hero, Skeleton, Boss
from view import View
from random import randint, choice


class Game():
    def __init__(self):
        self.moves = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}
        self.direction = 'right'
        self.view = View()
        self.map = Map()
        self.view.display_map(self.map.occupied_tile_position)
        self.hero = Hero(self.map.occupied_tile_position)
        self.game_start()
        self.view.master.mainloop()


    def game_start(self):
        self.hero_move_number = 0
        self.view.display_hero(self.hero.position, 'down')
        self.input_event()
        self.generate_skeletons()
        self.view.display_skeleton(self.skeleton_list)
        self.generate_boss()
        self.view.display_boss(self.boss.position)


# *********************Events**********************
    def input_event(self):
        self.view.master.bind('<s>', self.set_move)
        self.view.master.bind('<w>', self.set_move)
        self.view.master.bind('<a>', self.set_move)
        self.view.master.bind('<d>', self.set_move)
        self.view.master.bind('<space>', self.battle)

    def set_move(self, event):
        if event.char == 'w':
            self.hero.position, self.map.occupied_tile_position = self.hero.move(self.moves['up'],
                                                                                 self.map.occupied_tile_position)
            self.direction = 'up'
        elif event.char == 's':
            self.hero.position, self.map.occupied_tile_position = self.hero.move(self.moves['down'],
                                                                                 self.map.occupied_tile_position)
            self.direction = 'down'
        elif event.char == 'a':
            self.hero.position, self.map.occupied_tile_position = self.hero.move(self.moves['left'],
                                                                                 self.map.occupied_tile_position)
            self.direction = 'left'
        elif event.char == 'd':
            self.hero.position, self.map.occupied_tile_position = self.hero.move(self.moves['right'],
                                                                                 self.map.occupied_tile_position)
            self.direction = 'right'
        self.hero_move_number += 1
        self.view.display_hero(self.hero.position, self.direction)
        self.generate_enemy_moves()
        self.view.display_boss(self.boss.position)
        self.view.display_skeleton(self.skeleton_list)

    def generate_enemy_moves(self):
        if self.hero_move_number%2:
            self.boss.position, self.map.occupied_tile_position = self.boss.move(choice(list(self.moves.values())), self.map.occupied_tile_position)
            for skeleton in self.skeleton_list:
                skeleton.position, self.map.occupied_tile_position = skeleton.move(choice(list(self.moves.values())), self.map.occupied_tile_position)

    def battle(self, event):
        x_coord = self.hero.position[0]+self.moves[self.direction][0]
        y_coord = self.hero.position[1]+self.moves[self.direction][1]
        attack_coords = [x_coord, y_coord]
        attacked_enemy = None
        for skeleton in self.skeleton_list:
            if len(self.skeleton_list) != 0 and skeleton.position == attack_coords:
                attacked_enemy = skeleton
        try:
            if self.boss.position == attack_coords:
                attacked_enemy = self.boss
            if attacked_enemy == None:
                return
        except (NameError, AttributeError):
            return
        else:
            attacked_enemy.current_HP -= max(self.hero.stats[2] + randint(1,6) - attacked_enemy.stats[1], 0)
            self.hero.current_HP -= max(attacked_enemy.stats[2] + randint(1,6) - self.hero.stats[1], 0)
            print('enemy:' + str(attacked_enemy.current_HP) + '  hero:' + str(self.hero.current_HP))
        if self.hero.current_HP <= 0:
            self.game_over()
        elif attacked_enemy.current_HP <= 0:
            del self.view.ref_boss
            print('meghot ')

    def game_over(self):
        pass

# *****************Generate enemies*******************
    def generate_skeletons(self):
        skeleton_name_list = ['skeleton'+str(i) for i in range(self.map.number_of_skeletons)]
        self.skeleton_list = []
        for skeleton_name in skeleton_name_list:
            self.skeleton_name = Skeleton(self.map.wall_position)
            if skeleton_name[-1:] == '1':
                self.skeleton_name.has_key = True
            self.skeleton_list.append(self.skeleton_name)

    def generate_boss(self):
        self.boss = Boss(self.map.wall_position)

x = Game()

from model import Map, Hero, Skeleton, Boss
from view import View
from random import randint, choice


class Game():
    def __init__(self):
        self.direction = 'down'
        self.hero_stat_statusbar = None
        self.level = 1
        self.view = View(self.level)
        self.map = Map()
        self.hero = Hero(self.map.occupied_tile_position)
        self.game_start(self.level)
        self.view.master.mainloop()

    def game_start(self, level):
        self.hero_move_number = 0
        self.map.next_level_map()
        self.view.display_map(self.map.occupied_tile_position)
        self.view.statusbar_text(self.level, self.hero_stat_statusbar)
        self.hero.position = self.hero.randomize_position(self.map.occupied_tile_position)
        self.view.display_intro(self.level)
        self.generate_enemies(level)
        self.hero.restore_health()
        self.enemy_stat_statusbar = None
        self.input_event()

# *********************Events**********************
    def input_event(self):
        self.view.master.bind('<s>', self.set_move)
        self.view.master.bind('<w>', self.set_move)
        self.view.master.bind('<a>', self.set_move)
        self.view.master.bind('<d>', self.set_move)
        self.view.master.bind('<space>', self.battle)
        self.view.master.bind('<Escape>', self.quit)

    def set_move(self, event):
        if event.char == 'w':
            self.hero.position, self.map.occupied_tile_position = self.hero.move(
                self.hero.moves['up'], self.map.occupied_tile_position)
            self.direction = 'up'
        elif event.char == 's':
            self.hero.position, self.map.occupied_tile_position = self.hero.move(
                self.hero.moves['down'], self.map.occupied_tile_position)
            self.direction = 'down'
        elif event.char == 'a':
            self.hero.position, self.map.occupied_tile_position = self.hero.move(
                self.hero.moves['left'], self.map.occupied_tile_position)
            self.direction = 'left'
        elif event.char == 'd':
            self.hero.position, self.map.occupied_tile_position = self.hero.move(
                self.hero.moves['right'], self.map.occupied_tile_position)
            self.direction = 'right'
        self.hero_move_number += 1
        self.view.display_hero(self.hero.position, self.direction, self.hero.isDead)
        self.generate_enemy_moves()
        self.view.display_enemies(self.enemy_list)
        self.update_hero_status()
        self.enemy_stat_statusbar = None
        self.view.statusbar_text(self.level, self.hero_stat_statusbar)
        if self.hero_move_number > 0:
            self.start()


    def generate_enemy_moves(self):
        if self.hero_move_number%2:
            for enemy in self.enemy_list:
                enemy.position, self.map.occupied_tile_position = enemy.move(
                    choice(list(enemy.moves.values())), self.map.occupied_tile_position)

    def battle(self, event):
        x_coord = self.hero.position[0]+self.hero.moves[self.direction][0]
        y_coord = self.hero.position[1]+self.hero.moves[self.direction][1]
        attack_coords = [x_coord, y_coord]
        attacked_enemy = None
        if len(self.enemy_list) != 0:
            for enemy in self.enemy_list:
                if enemy.position == attack_coords:
                    attacked_enemy = enemy
        if attacked_enemy == None:
            return
        attacked_enemy.current_HP -= max(self.hero.stats[2] + randint(1,6) - attacked_enemy.stats[1], 0)
        self.hero.current_HP -= max(attacked_enemy.stats[2] + randint(1,6) - self.hero.stats[1], 0)
        self.view.display_attack(self.hero.position, attacked_enemy.position)
        self.update_hero_status()
        self.update_enemy_stats(attacked_enemy)
        self.view.statusbar_text(self.level, self.hero_stat_statusbar, self.enemy_stat_statusbar)
        if attacked_enemy.current_HP <= 0:
            self.kill_enemy(attacked_enemy)
        if self.hero.current_HP <= 0:
            self.game_over()

    def kill_enemy(self, attacked_enemy):
        self.map.occupied_tile_position[attacked_enemy.position[1]][attacked_enemy.position[0]] = 0
        self.enemy_list.remove(attacked_enemy)
        self.view.display_enemies(self.enemy_list)
        self.view.display_kill(attacked_enemy.position)
        self.hero.level_up()
        if attacked_enemy.has_key == True:
            self.hero.has_key = True
        if type(attacked_enemy) == Boss:
            self.hero.has_killed_boss = True
        if self.hero.has_key == True and self.hero.has_killed_boss == True:
            self.new_game()

    def game_over(self):
        self.enemy_list = []
        self.hero.isDead = True
        self.view.display_enemies(self.enemy_list)
        self.view.display_hero(self.hero.position, self.direction, self.hero.isDead)
        self.view.display_game_over()

    def new_game(self):
        self.level += 1
        self.game_start(self.level)
        self.hero.has_killed_boss = False
        self.hero.has_key = False

    def quit(self, event):
        self.view.master.destroy()

    def start(self):
        self.view.delete_pictures()
        self.view.display_hero(self.hero.position, self.direction, self.hero.isDead)
        self.view.display_enemies(self.enemy_list)

    def update_hero_status(self):
        self.hero_stat_statusbar=self.hero.stats[:]
        self.hero_stat_statusbar.append(self.hero.current_HP)
        self.hero_stat_statusbar.append(self.hero.has_key)

    def update_enemy_stats(self,attacked_enemy):
        self.enemy_stat_statusbar=attacked_enemy.stats[:]
        self.enemy_stat_statusbar.append(attacked_enemy.current_HP)
        if type(attacked_enemy) == Boss:
            self.enemy_stat_statusbar.append('boss')
        else:
            self.enemy_stat_statusbar.append('skeleton')

# *****************Generate enemies*******************
    def generate_enemies(self, level):
        self.boss = Boss(self.map.wall_position, level)
        self.enemy_list = [self.boss]
        for i in range(self.map.number_of_skeletons):
            skeleton_name = 'skeleton'+str(i)
            self.skeleton_name = Skeleton(self.map.wall_position, level)
            if skeleton_name[-1:] == '0':
                self.skeleton_name.has_key = True
            self.enemy_list.append(self.skeleton_name)

x = Game()

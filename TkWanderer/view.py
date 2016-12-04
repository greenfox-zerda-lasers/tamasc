from tkinter import *
from model import Boss

class View():
    def __init__(self, level):
        self.master = Tk()
        self.canvas = Canvas(width=722, height=722, bg='black')
        self.canvas.pack(side=LEFT, padx=5, pady=5)
        self.statusbar = Canvas(width=300, height=720, bg='#E6983E')
        self.statusbar.pack(side=RIGHT, padx=5, pady=5)
        self.statusbar_text(level)
        self.skeleton = PhotoImage(file="skeleton.png")
        self.boss = PhotoImage(file="boss.png")
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")
        self.game_over = PhotoImage(file="game_over.png")
        self.spark = PhotoImage(file="spark.png")
        self.skull = PhotoImage(file="skull.png")


    def display_map(self, wall_position):
        for i in range(len(wall_position[0])):
            for j in range(len(wall_position)):
                if wall_position[j][i] == 1:
                    self.canvas.create_image(38+i*72, 38+j*72, image=self.wall)
                else:
                    self.canvas.create_image(38+i*72, 38+j*72, image=self.floor)

    def display_hero(self, position, direction='down', isDead=False):
        self.canvas.delete('hero')
        file_name = 'hero-' + direction + '.png'
        if isDead:
            file_name = 'skull.png'
        self.hero = PhotoImage(file=file_name)
        self.canvas.create_image(38+position[0]*72, 38+position[1]*72, image=self.hero, tag='hero')

    def display_enemies(self, enemy_list):
        self.canvas.delete('enemy')
        for enemy in enemy_list:
            if type(enemy) == Boss:
                self.canvas.create_image(38+enemy.position[0]*72, 38+enemy.position[1]*72, image=self.boss, tag='enemy')
            else:
                self.canvas.create_image(38+enemy.position[0]*72, 38+enemy.position[1]*72, image=self.skeleton, tag='enemy')

    def display_game_over(self):
        self.canvas.create_image(360, 330, image=self.game_over)

    def display_intro(self, level):
        if level == 1:
            self.intro = PhotoImage(file="tkwanderer.png")
        else:
            self.intro = PhotoImage(file="next_level.png")
        self.intro_object = self.canvas.create_image(360, 330, image=self.intro, tag='logo')

    def delete_pictures(self):
        self.canvas.delete('logo')
        self.canvas.delete('spark')
        self.canvas.delete('skull')

    def display_attack(self, hero_position, enemy_position):
        x = (hero_position[0]+enemy_position[0])/2*72+38
        y = (hero_position[1]+enemy_position[1])/2*72+38
        self.canvas.create_image(x, y, anchor=CENTER, image=self.spark, tag='spark')

    def display_kill(self, enemy_position):
        x = enemy_position[0]*72+38
        y = enemy_position[1]*72+38
        self.canvas.create_image(x, y, anchor=CENTER, image=self.skull, tag='skull')

    def statusbar_text(self, level, hero_stats=None, enemy_stats=None):
        self.statusbar.delete('statusbar')
        level = 'Level:' + str(level)
        self.statusbar.create_text(150, 50, font=("fixedsys", 33, 'bold'), text='TkWanderer', fill='#2D2B1F', tag='statusbar')
        self.statusbar.create_text(150, 150, font=("fixedsys", 25, 'bold'), text=level, fill='#2D2B1F', tag='statusbar')
        if hero_stats == None:
            return
        hero_stat_text = 'HP  DP  SP\n' + str(int(hero_stats[0])).zfill(2) + '  ' + str(int(hero_stats[1])).zfill(2)+ '  ' + str(int(hero_stats[2])).zfill(2)
        hero_current_hp = 'Current HP: '+ str(int(hero_stats[3]))
        self.hero_img = PhotoImage(file='hero-down.png')
        self.statusbar.create_image(50, 265, image=self.hero_img, tag='statusbar')
        self.statusbar.create_text(190, 265, font=("fixedsys", 23), text=hero_stat_text, fill='#2D2B1F', tag='statusbar')
        self.statusbar.create_text(145, 325, font=("fixedsys", 23), text=hero_current_hp, fill='#2D2B1F', tag='statusbar')
        has_key_text = 'Has key: ' + str(hero_stats[4])
        self.statusbar.create_text(150, 365, font=("fixedsys", 23), text=has_key_text, fill='#2D2B1F', tag='statusbar')
        if enemy_stats == None:
            return
        elif enemy_stats[4] == 'boss':
            self.enemy_img = self.boss
        else:
            self.enemy_img = self.skeleton
        enemy_stat_text = 'HP  DP  SP\n' + str(int(enemy_stats[0])).zfill(2) + '  ' + str(int(enemy_stats[1])).zfill(2)+ '  ' + str(int(enemy_stats[2])).zfill(2)
        enemy_current_hp = 'Current HP: '+ str(int(enemy_stats[3]))
        self.statusbar.create_image(50, 465, image=self.enemy_img, tag='statusbar')
        self.statusbar.create_text(190, 465, font=("fixedsys", 23), text=enemy_stat_text, fill='#2D2B1F', tag='statusbar')
        self.statusbar.create_text(145, 525, font=("fixedsys", 23), text=enemy_current_hp, fill='#2D2B1F', tag='statusbar')

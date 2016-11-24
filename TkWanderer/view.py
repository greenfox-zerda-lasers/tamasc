from tkinter import *
from model import Boss
import time

class View():
    def __init__(self):
        self.master = Tk()
        self.canvas = Canvas(width=900, height=800, bg='white')
        self.canvas.pack()


    def display_map(self, wall_position):
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")
        for i in range(len(wall_position[0])):
            for j in range(len(wall_position)):
                if wall_position[j][i] == 1:
                    self.canvas.create_image(36+i*72, 36+j*72, image=self.wall)
                else:
                    self.canvas.create_image(36+i*72, 36+j*72, image=self.floor)

    def display_hero(self, position, direction='down', isDead=False):
        file_name = 'hero-' + direction + '.png'
        if isDead:
            file_name = 'skull.png'
        self.hero = PhotoImage(file=file_name)
        self.canvas.create_image(36+position[0]*72, 36+position[1]*72, image=self.hero)

    def display_enemies(self, enemy_list):
        self.skeleton = PhotoImage(file="skeleton.png")
        self.boss = PhotoImage(file="boss.png")
        for enemy in enemy_list:
            if type(enemy) == Boss:
                self.canvas.create_image(36+enemy.position[0]*72, 36+enemy.position[1]*72, image=self.boss)
            else:
                self.canvas.create_image(36+enemy.position[0]*72, 36+enemy.position[1]*72, image=self.skeleton)

    def display_game_over(self):
        self.game_over = PhotoImage(file="game_over.png")
        self.canvas.create_image(360, 330, image=self.game_over)

    def display_intro(self, level):
        if level == 1:
            self.intro = PhotoImage(file="tkwanderer.png")
        else:
            self.intro = PhotoImage(file="next_level.png")
        self.intro_object = self.canvas.create_image(360, 330, image=self.intro, tag='logo')

    def delete_intro(self):
        self.canvas.delete('logo')

    def display_attack(self, hero_position, enemy_position):
        self.spark = PhotoImage(file="spark.png")
        x = (hero_position[0]+enemy_position[0])/2*72
        y = (hero_position[1]+enemy_position[1])/2*72
        self.canvas.create_image(x, y, image=self.spark)

from tkinter import *


class View():
    def __init__(self):
        self.master = Tk()
        self.canvas = Canvas(width=900, height=800, bg='white')
        self.canvas.pack()

    def display_map(self, tile_position):
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")
        for i in range(len(tile_position[0])):
            for j in range(len(tile_position)):
                if tile_position[j][i] == 1:
                    self.canvas.create_image(36+i*72, 36+j*72, image=self.wall)
                else:
                    self.canvas.create_image(36+i*72, 36+j*72, image=self.floor)

    def display_hero(self, position, direction):
        file_name = 'hero-' + direction + '.png'
        self.hero = PhotoImage(file=file_name)
        self.canvas.create_image(36+position[0]*72, 36+position[1]*72, image=self.hero)

    def display_skeleton(self, skeleton_list):
        self.skeleton = PhotoImage(file="skeleton.png")
        for skeleton in skeleton_list:
            self.canvas.create_image(36+skeleton.position[0]*72, 36+skeleton.position[1]*72, image=self.skeleton)

    def display_boss(self, position,):
        self.boss = PhotoImage(file="boss.png")
        self.canvas.create_image(36+position[0]*72, 36+position[1]*72, image=self.boss)

from model import Map, Hero
from view import View


class Game():
    def __init__(self):
        self.view = View()
        self.map = Map()
        self.view.display_map(self.map.tile_position)
        self.hero = Hero(self.map.tile_position)
        self.game_loop()
        self.view.master.mainloop()

    def game_loop(self):
        # while self.hero.stats[0] > 0:
        self.view.display_hero(self.hero.position)
        self.input_event()



    def input_event(self):
        self.view.master.bind('<s>', self.set_move)
        self.view.master.bind('<w>', self.set_move)
        self.view.master.bind('<a>', self.set_move)
        self.view.master.bind('<d>', self.set_move)

    def set_move(self, event):
        if event.char == 'w':
            self.hero.position = self.hero.move([0, -1], self.map.tile_position)
        elif event.char == 's':
            self.hero.position = self.hero.move([0, 1], self.map.tile_position)
        elif event.char == 'a':
            self.hero.position = self.hero.move([-1, 0], self.map.tile_position)
        elif event.char == 'd':
            self.hero.position = self.hero.move([1, 0], self.map.tile_position)
        print(self.hero.position)
        self.view.display_hero(self.hero.position)

x = Game()

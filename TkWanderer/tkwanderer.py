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
        self.view.display_hero(self.hero.position)



x = Game()

import game
import objects as OBJ
import resources as R
import basic
import pygame as pg


class Game(game.Game):
    def start(self):
        self.move = pg.Vector2(0,0)
        self.btn = OBJ.ButtonImg(pg.Vector2(50,50), R.IMG_BLACK, R.IMG_BLACK, R.IMG_BLACK, "H", R.NORMAL_FONT, R.WHITE, pg.Vector2(22,15))
    def update(self):
        self.btn.update(self.deltaTime, self.mouse)

        if self.mouse.SLIDE.x == 1:
            self.move.x = 1
            self.move.y = 0
        elif self.mouse.SLIDE.x == -1:
            self.move.x = -1
            self.move.y = 0
        if self.mouse.SLIDE.y == 1:
            self.move.y = 1
            self.move.x = 0
        elif self.mouse.SLIDE.y == -1:
            self.move.y = -1
            self.move.x = 0
        
        self.btn.position.x += self.move.x * 200 * self.deltaTime
        self.btn.position.y += self.move.y * 200 * self.deltaTime
        self.mouse.print_info()

    def draw(self):
        self.btn.draw(self.screen)



if __name__ == "__main__":
    game = Game()
    game.mainloop()

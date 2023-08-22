import game
import objects as OBJ
import resources as R
import basic
import pygame as pg


class Game(game.Game):
    def start(self):
        self.move = pg.Vector2(0,0)


        self.btn2 = OBJ.ButtonImg(pg.Vector2(0,0), R.IMG_BLACK, R.IMG_BLACK, R.IMG_BLACK, "H", R.NORMAL_FONT, R.WHITE, pg.Vector2(22,15), "TL")

        self.btn = OBJ.ButtonImg(pg.Vector2(R.WIDTH/2,R.HEIGHT/2), R.IMG_BLACK, R.IMG_BLACK, R.IMG_BLACK, "H", R.NORMAL_FONT, R.WHITE, pg.Vector2(22,15))
    def update(self):
        self.btn.update(self.deltaTime, self.mouse)
        self.btn2.update(self.deltaTime, self.mouse)

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

        self.btn.setPosition((self.btn.Position("x") + self.move.x * 200 * self.deltaTime, self.btn.Position("y") + self.move.y * 200 * self.deltaTime))
        self.btn2.setPosition((self.btn2.Position("x") + self.move.x * 200 * self.deltaTime, self.btn2.Position("y") + self.move.y * 200 * self.deltaTime))

    def draw(self):
        self.btn.draw(self.screen)
        self.btn2.draw(self.screen)



if __name__ == "__main__":
    game = Game()
    game.mainloop()

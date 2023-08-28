import game
import objects as OBJ
import resources as R
import basic
import pygame as pg


class Game(game.Game):
    def start(self):
        self.move = pg.Vector2(0,0)

        self.Camera = OBJ.Camera(pg.Vector2(R.WIDTH/2, R.HEIGHT/2), pg.Vector2(R.WIDTH, R.HEIGHT))

        self.player = OBJ.NodeImg(pg.Vector2((R.WIDTH - R.IMG_BLACK.get_width())/2, (R.HEIGHT- R.IMG_BLACK.get_height())/2), R.IMG_BLACK)
        
        self.btn2 = OBJ.ButtonImg(pg.Vector2(0,0), R.IMG_BLACK, R.IMG_BLACK, R.IMG_BLACK, "H", R.NORMAL_FONT, R.WHITE, pg.Vector2(22,15))

        self.btn = OBJ.ButtonImg(pg.Vector2(R.WIDTH/2,20), R.IMG_BLACK, R.IMG_BLACK, R.IMG_BLACK, "H", R.NORMAL_FONT, R.WHITE, pg.Vector2(22,15))
    def update(self):
        self.btn.update(self.deltaTime, self.mouse)
        self.btn2.update(self.deltaTime, self.mouse)
        self.player.update(self.deltaTime)

        if self.keys[pg.K_RIGHT]:
            self.player.position.x += 100 *self.deltaTime
        elif self.keys[pg.K_LEFT]:
            self.player.position.x += -100 *self.deltaTime
        if self.keys[pg.K_DOWN]:
            self.player.position.y += 100 *self.deltaTime
        elif self.keys[pg.K_UP]:
            self.player.position.y += -100 *self.deltaTime
        
        self.Camera.positionC = pg.Vector2(self.player.position.x + R.IMG_BLACK.get_width()/2,
                                           self.player.position.y + R.IMG_BLACK.get_height()/2)

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
        self.btn2.position.x += self.move.x * 200 * self.deltaTime
        self.btn2.position.y += self.move.y * 200 * self.deltaTime

    def draw(self):
        self.btn.draw(self.screen, self.Camera)
        self.btn2.draw(self.screen, self.Camera)
        self.player.draw(self.screen, self.Camera)



if __name__ == "__main__":
    game = Game()
    game.mainloop()

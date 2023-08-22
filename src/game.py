import pygame
import resources as R
import basic
import os
pygame.init()

class Game:
    def __init__(self) -> None:
        
        # Window and screen
        self.window = pygame.display.set_mode((basic.set_real(R.WIDTH), basic.set_real(R.HEIGHT)), R.FULLSCREEN)
        pygame.display.set_caption("Game")
        self.screen = pygame.Surface((R.WIDTH, R.HEIGHT))

        # Pygame variables
        self.clock = pygame.time.Clock()
        self.running = True
        self.deltaTime = 0
        self.offset = pygame.Vector2(0,0)
        self.fix = 1
        self.mouse = Mouse()

        # Your Variables
        self.start()
    
    def start(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
    def mainloop(self):
        while self.running:
            self.mouse.DOWN = False
            self.mouse.UP = False
            self.mouse.MOTION = False
            self.mouse.SLIDE = pygame.Vector2(0,0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse.DOWN = True
                    self.mouse.wasDOWN = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.mouse.wasDOWN:
                        self.mouse.wasDOWN = False
                        self.mouse.isSliding()
                    self.mouse.UP = True
                if event.type == pygame.MOUSEMOTION:
                    self.mouse.MOTION = True

            self.mouse.realposition.x, self.mouse.realposition.y = pygame.mouse.get_pos()
            self.mouse.position.x = (self.mouse.realposition.x - self.offset.x) / self.fix
            self.mouse.position.y = (self.mouse.realposition.y - self.offset.y) / self.fix
            if self.mouse.DOWN:
                self.mouse.wasDOWNPosition.x = self.mouse.position.x
                self.mouse.wasDOWNPosition.y = self.mouse.position.y

            self.keys = pygame.key.get_pressed()

            self.base_update()
            self.update()
            
            self.base_draw()
            self.draw()
            self.end_draw()

            self.deltaTime = self.clock.tick(60) / 1000.0
            pygame.display.update()
    def base_update(self):
        self.update_fix()
    def base_draw(self):
        self.screen.fill((255, 255, 255))
        self.window.fill((0, 0, 0))
    def end_draw(self):
        self.window.blit(pygame.transform.scale(self.screen, ( int(R.WIDTH*self.fix), int(R.HEIGHT*self.fix) )), self.offset)

    def update_fix(self):
        height = self.window.get_height()
        width = self.window.get_width()
        if (height / R.HEIGHT) <= (width/R.WIDTH):
            self.fix = (height / R.HEIGHT)
            self.offset.x = (width - (R.WIDTH * self.fix)) / 2
            self.offset.y = 0
        else:
            self.fix = (width / R.WIDTH)
            self.offset.x = 0
            self.offset.y = (height - (R.HEIGHT * self.fix)) / 2

class Mouse:
    def __init__(self) -> None:
        self.position = pygame.Vector2()
        self.realposition = pygame.Vector2()
        self.DOWN = False
        self.UP = False
        self.MOTION = False
        self.SLIDE = pygame.Vector2(0,0)

        self.wasDOWN = False
        self.wasDOWNPosition = pygame.Vector2(0,0)

    def isSliding(self):
        temp_position = self.position - self.wasDOWNPosition
        if abs(temp_position.x) > abs(temp_position.y):
            if temp_position.x > R.WIDTH/4:
                self.SLIDE.x = 1
            elif temp_position.x < -R.WIDTH/4:
                self.SLIDE.x = -1
        else:
            if temp_position.y > R.HEIGHT/4:
                self.SLIDE.y = 1
            elif temp_position.y < -R.HEIGHT/4:
                self.SLIDE.y = -1



    def print_info(self):
        os.system("clear")
        print(f"Position: {self.position}")
        if self.DOWN:
            print("Pressed")
        elif self.UP:
            print("Released")
        else:
            print("")
        if self.MOTION:
            print("Movement")
        else:
            print()
        print(f"wasDOWN {self.wasDOWN}, {self.wasDOWNPosition}")
        print(f"Slide: {self.SLIDE}")
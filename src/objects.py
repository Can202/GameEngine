import pygame
import basic
import copy

class NodeRect:
    def __init__(self, _rect, _color) -> None:
        self.rect = _rect
        self.color = _color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class NodeImg(NodeRect):
    def __init__(self, _position, _image, type="C") -> None:
        super().__init__(_image.get_rect(), (100,100,200))
        self.image = _image
        if type == "C":
            self.rect = pygame.Rect(_position.x - _image.get_rect().x/2, _position.y - _image.get_rect().y/2, _image.get_rect().x, _image.get_rect().y)
        else:
            self.rect = pygame.Rect(_position.x, _position.y, _image.get_rect().x, _image.get_rect().y)
        self.positionTL = pygame.Vector2(self.rect.left, self.rect.top)
        self.positionC = pygame.Vector2(self.rect.centerx, self.rect.centery)
    
    def Position (self, value="xy", type="C"):
        if type == "C":
            if value == "xy":
                return self.positionC
            elif value == "x":
                return self.positionC.x
            elif value == "y":
                return self.positionC.y
        if type == "TL":
            if value == "xy":
                return self.positionTL
            elif value == "x":
                return self.positionTL.x
            elif value == "y":
                return self.positionTL.y

    def setPosition(self, Vector = pygame.Vector2(0,0),type="C"):
        if type == "C":
            self.rect.center = Vector
        elif type == "TL":
            self.rect.topleft = Vector
        self.positionTL = pygame.Vector2(self.rect.left, self.rect.top)
        self.positionC = pygame.Vector2(self.rect.centerx, self.rect.centery)
    def setPositionX(self, X = 0,type="C"):
        if type == "C":
            self.rect.centerx = X
        elif type == "TL":
            self.rect.left = X
        self.positionTL = pygame.Vector2(self.rect.left, self.rect.top)
        self.positionC = pygame.Vector2(self.rect.centerx, self.rect.centery)
    def setPositionY(self, Y = 0,type="C"):
        if type == "C":
            self.rect.centery = Y
        elif type == "TL":
            self.rect.top = Y
        self.positionTL = pygame.Vector2(self.rect.left, self.rect.top)
        self.positionC = pygame.Vector2(self.rect.centerx, self.rect.centery)

    def update(self, deltaTime):
        pass
    def draw(self, screen):
        screen.blit(self.image, self.positionTL)
    def draw_collision(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Timer:
    def __init__(self, _count_to) -> None:
        self.time = 0
        self.timing = False
        self.count_to = _count_to

    def update(self, deltaTime):
        if self.timing:
            if self.time > self.count_to:
                self.timing = False
                self.time = 0
            self.time += 1 * deltaTime
        else:
            self.time = 0


class ButtonImg(NodeImg):
    def __init__(self,
                 _position:pygame.Vector2,
                 _image:pygame.image,
                 _imagehover:pygame.image,
                 _imagepressed:pygame.image,
                 _text:str, _font:pygame.font, _color:pygame.color, _distance:pygame.Vector2, _type="C"):
        super().__init__(_position, _image, _type)
        self.distanceText = _distance
        self.text = Text(self.Position("xy", "TL") + _distance, _text, _font, _color)
        self.just_pressed = False
        self.pressed_and_still = False
        self.pressed_and_still_no_position = False
        self.was_pressed_and_still = False
        self.normal_image = self.image
        self.image_hover = _imagehover
        self.image_pressed = _imagepressed
    def change_all_img(self,_image:pygame.image):
        self.image = _image
        self.normal_image = _image
        self.image_hover = _image
        self.image_pressed = _image
    def update(self, deltaTime, mouse):
        self.text.position = self.positionTL + self.distanceText
        self.just_pressed = False
        if (self.rect.left < mouse.position.x < self.rect.right) and (self.rect.top < mouse.position.y < self.rect.bottom):
            if basic.platform() != "android":
                self.image = self.image_hover
            else:
                self.image = self.normal_image
            if mouse.wasDOWN:
                self.was_pressed_and_still = True
            if mouse.DOWN:
                self.image = self.image_pressed
                self.just_pressed = True
                self.pressed_and_still = True
                self.pressed_and_still_no_position = True
            if mouse.UP:
                self.pressed_and_still = False
                self.was_pressed_and_still = False
                
            
        elif (self.rect.left < mouse.position.x < self.rect.right) and (self.rect.top < mouse.position.y < self.rect.bottom):
            if basic.platform() != "android":
                self.image = self.image_hover
            else:
                self.image = self.normal_image
            if mouse.wasDOWN:
                self.was_pressed_and_still = True
            if mouse.DOWN:
                self.image = self.image_pressed
                self.just_pressed = True
                self.pressed_and_still = True
                self.pressed_and_still_no_position = True
            if mouse.UP:
                self.pressed_and_still = False
                self.was_pressed_and_still = False
        else:
            self.pressed_and_still = False
            self.was_pressed_and_still = False
            self.image = self.normal_image
        if mouse.UP:
            self.pressed_and_still_no_position = False

    
    def draw(self, screen):
        super().draw(screen)
        self.text.draw(screen)

class Text():
    def __init__(self, _position:pygame.Vector2, _text:str, _font:pygame.font, _color:pygame.color):
        self.text = _text
        self.position = _position
        self.font = _font
        self.color = _color

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, self.position)

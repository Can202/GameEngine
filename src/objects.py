import pygame
import basic
import copy

class NodeRect:
    def __init__(self, _position, _rect, _color) -> None:
        self.position = _position
        self.rect = _rect
        self.color = _color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class NodeImg(NodeRect):
    def __init__(self, _position, _image) -> None:
        super().__init__(_position, _image.get_rect(), (100,100,200))
        
        self.image = _image

    def update(self, deltaTime):
        pass
    def draw(self, screen):
        screen.blit(self.image, self.position)
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
                 _text:str, _font:pygame.font, _color:pygame.color, _distance:pygame.Vector2):
        super().__init__(_position, _image)
        self.distanceText = _distance
        self.text = Text(_position + _distance, _text, _font, _color)
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
        self.text.position = self.position + self.distanceText
        self.just_pressed = False
        self.rect = self.image.get_rect()
        self.rect.left += self.position.x
        self.rect.top += self.position.y
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

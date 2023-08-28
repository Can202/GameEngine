import pygame
import basic
import copy

class NodeRect:
    def __init__(self, _rect, _color) -> None:
        self.rect = _rect
        self.color = _color
    def draw(self, screen, camera):
        #pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.color, pygame.Rect(
            camera.getPositionFromCamera(pygame.Vector2(self.rect.width,0)).x,
            camera.getPositionFromCamera(pygame.Vector2(0,self.rect.height)).y, 
            self.rect.width, self.rect.height
            ))

class NodeImg(NodeRect):
    def __init__(self, _position, _image) -> None:
        super().__init__(_image.get_rect(), (100,100,200))
        self.image = _image
        self.rect = pygame.Rect(_position.x, _position.y, _image.get_rect().x, _image.get_rect().y)
        self.position = _position
    
    def update(self, deltaTime):
        pass
    def draw(self, screen, camera):
        screen.blit(self.image, camera.getPositionFromCamera(self.position))
    def draw_collision(self, screen, camera):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            camera.getPositionFromCamera(self.position).x,
            camera.getPositionFromCamera(self.position).y, 
            self.rect.width, self.rect.height
            ))

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
        self.text = Text(self.position + _distance, _text, _font, _color)
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

    
    def draw(self, screen, camera):
        super().draw(screen, camera)
        self.text.draw(screen, camera)

class Text():
    def __init__(self, _position:pygame.Vector2, _text:str, _font:pygame.font, _color:pygame.color):
        self.text = _text
        self.position = _position
        self.font = _font
        self.color = _color

    def draw(self, screen, camera):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, camera.getPositionFromCamera(self.position))

class Camera():
    def __init__(self, _position = pygame.Vector2(0,0), _size = pygame.Vector2(0,0)) -> None:
        self.positionC = _position
        self.size = _size
    
    def getPositionFromCamera(self, objectposition = pygame.Vector2(0,0)):
        return pygame.Vector2(
            objectposition.x - (self.positionC.x - self.size.x/2),
            objectposition.y - (self.positionC.y - self.size.y/2))
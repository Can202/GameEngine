import pygame
from os import environ
from sys import platform as _sys_platform

pygame.mixer.init()
pygame.font.init()

def load_font(url, size):
    return pygame.font.Font(f"{S_PATH}{url}", size)

def load_image(url):
    return pygame.image.load(f"{S_PATH}{url}")

def load_sound(url):
    pygame.mixer.Sound(f"{S_PATH}{url}")

def resize_image(image, width, height):
    return pygame.transform.scale(image, (width, height))

def platform():
    if 'ANDROID_ARGUMENT' in environ:
        return "android"
    elif _sys_platform in ('linux', 'linux2','linux3'):
        return "linux"
    elif _sys_platform in ('win32', 'cygwin'):
        return 'win'
    else:
        return "else"

def getPath():
    if platform()=="android":
        return "/data/data/com.can202.readtime/files/app/"
    else:
        return ""
    

S_PATH = getPath()

def set_real(number):
    if platform() == "android":
        return number
    else:
        return 0
    
def setFullscreen(boolean: bool):
    if boolean:
        return pygame.FULLSCREEN
    else:
        if platform() == "android":
            return pygame.FULLSCREEN
        else:
            return pygame.RESIZABLE
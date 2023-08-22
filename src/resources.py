from basic import *

# Globals
WIDTH = 500
HEIGHT = 500
FULLSCREEN = setFullscreen(False)

# Images
IMG_BASICCUBE = resize_image(load_image("media/blank.png"), 60, 60)
IMG_BLACK = resize_image(load_image("media/blackimg.png"), 60, 60)

# Sounds
SOUND_GOOD = load_sound("media/good.mp3")

# Fonts
NORMAL_FONT = load_font("media/SimplyMono-Bold.ttf", 25)

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
DARK_GREEN = (0,100,0)

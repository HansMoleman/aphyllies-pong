
### Game ##
#
# EXEC:
# DEPN:
#
# This module is responsible for defining all game variables
# and methods.
#
# ---
#  ver
# ---
##

from kivy.core.window import Window
from kivy.config import Config


# Game Variables
#-----#

# Core
#Window.maximize()
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")
SCREEN_SIZE = Window.size
BGD_COLOUR = (1, 1, 1, 1)

# Ball
b_wid = round((SCREEN_SIZE[0] * 0.05), 0)
b_hei = b_wid
b_x = (SCREEN_SIZE[0] / 2) - (b_wid / 2)
b_y = (SCREEN_SIZE[1] / 2) - (b_hei / 2)
BALL_COLOUR = (0, 0, 0, 1)
BALL_OFFSET = (b_x, b_y)
BALL_SIZE = (b_wid, b_hei)
BALL_SPEED = (8, 8)

# Paddle
p_wid = round((SCREEN_SIZE[0] * 0.05), 0)
p_hei = round((SCREEN_SIZE[1] * 0.27), 0)
p_x = round((SCREEN_SIZE[0] * 0.05), 0)
p_y = (SCREEN_SIZE[1] / 2) - (p_hei / 2)
PADDLE_COLOUR = (1, 1, 1, 1)
PADDLE_OFFSET = (p_x, p_y)
PADDLE_SIZE = (p_wid, p_hei)
PADDLE_SPEED = (0, 6)

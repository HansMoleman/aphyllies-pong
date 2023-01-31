
### Game ##
#
#
#
#
##

from kivy.core.window import Window


## Window & Root Screen
Window.maximize()
WINDOW_WIDTH  =  Window.size[0]
WINDOW_HEIGHT =  Window.size[1]
BGD_COLOUR    =  (0, 0, 0, 1)


## Paddle
PADDLE_COLOUR =  (1, 1, 1, 0)
PADDLE_WIDTH  =  round((WINDOW_WIDTH * 0.05), 0)
PADDLE_HEIGHT =  round((WINDOW_HEIGHT * 0.27), 0)
PADDLE_X 	 =  round((WINDOW_WIDTH * 0.05), 0)
PADDLE_Y 	 =  (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)

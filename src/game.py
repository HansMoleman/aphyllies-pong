
### Game ##
#
#
#
#
##

from kivy.core.window import Window


## Window & Root Screen
WINDOW_WIDTH  =  Window.size[0]
WINDOW_HEIGHT =  Window.size[1]
print("{} x {}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
BGD_COLOUR    =  (0, 0, 0, 1)


## Ball
BALL_COLOUR   =  (1, 1, 1, 0)
BALL_WIDTH    =  round((WINDOW_WIDTH * 0.05), 0)
BALL_HEIGHT   =  BALL_WIDTH
BALL_X        =  (WINDOW_WIDTH / 2) - (BALL_WIDTH / 2)
BALL_Y        =  (WINDOW_HEIGHT / 2) - (BALL_HEIGHT / 2)
BALL_SPEED    =  (8, 8)


## Paddle
PADDLE_COLOUR =  (1, 1, 1, 0)
PADDLE_WIDTH  =  round((WINDOW_WIDTH * 0.05), 0)
PADDLE_HEIGHT =  round((WINDOW_HEIGHT * 0.27), 0)
PADDLE_X 	  =  round((WINDOW_WIDTH * 0.05), 0)
PADDLE_Y 	  =  (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
PADDLE_SPEED  =  (0, 6)

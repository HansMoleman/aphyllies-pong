
### Pong ##
#
# EXEC:
# DEPN:
#
# This is the main file for the system.
#
# ---
#  ver-1.00
# ---
##


from kivy.app import App
from kivy.uix.label import Label
from vector2D import Vector2D as V2D
from frame import Frame
import game
from paddle import Paddle


class Pong(App):
	
	def build(self):

		frame = Frame(pos=(0, 0), size=game.SCREEN_SIZE)

		right_paddle_x = game.SCREEN_SIZE[0] - game.PADDLE_OFFSET[0] - game.PADDLE_SIZE[0]
		right_paddle_y = game.PADDLE_OFFSET[1]
		paddle_r = Paddle(pos=(right_paddle_x, right_paddle_y))

		left_paddle_x = game.PADDLE_OFFSET[0]
		left_paddle_y = game.PADDLE_OFFSET[1]
		paddle_l = Paddle(pos=(left_paddle_x, left_paddle_y))

		frame.addWidget(paddle_r)
		frame.addWidget(paddle_l)

		return frame


Pong().run()
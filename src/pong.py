
### Pong ##
#
# EXEC:
# DEPN:
#
# Yeet.
# 
# ---
#  ver.
# ---
##


from kivy.config import Config
Config.set("graphics", "resizable", "0")

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from ball import Ball
from paddle import Paddle
import game


class RootScreen(Widget):
	
	def __init__(self, **kwargs):
		super(RootScreen, self).__init__(**kwargs)

		self._ball = Ball()
		self._ball.setSpeed(game.BALL_SPEED)
		
		padl_r_x = (game.WINDOW_WIDTH - game.PADDLE_WIDTH - game.PADDLE_X)
		padl_l_x = game.PADDLE_X
		padl_y = game.PADDLE_Y
		self._paddle_r = Paddle(pos=(padl_r_x, padl_y))
		self._paddle_l = Paddle(pos=(padl_l_x, padl_y))
		self._paddle_l.setClickable(False)
		
		self.add_widget(self._ball)
		self.add_widget(self._paddle_r)
		self.add_widget(self._paddle_l)
	

	def update(self, *args):
		#padl_l = self._paddle_l.pos
		#padl_r = self._paddle_r.pos
		self._ball.updateState(self._paddle_l, self._paddle_r)


class Pong(App):
	
	def build(self):
		root = RootScreen()
		Clock.schedule_interval(root.update, (1/60))
		return root
	

Pong().run()
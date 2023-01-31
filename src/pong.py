
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


from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.core.window import Window
from paddle import Paddle
import game


class RootScreen(Widget):
	
	def __init__(self, **kwargs):
		super(RootScreen, self).__init__(**kwargs)
		
		padl_r_x = (game.WINDOW_WIDTH - game.PADDLE_WIDTH - game.PADDLE_X)
		padl_l_x = game.PADDLE_X
		padl_y = game.PADDLE_Y
		self._paddle_r = Paddle(pos=(padl_r_x, padl_y))
		self._paddle_l = Paddle(pos=(padl_l_x, padl_y))
		self._paddle_l.setClickable(False)
		
		self.add_widget(self._paddle_r)
		self.add_widget(self._paddle_l)


class Pong(App):
	
	def build(self):
		return RootScreen()
	

Pong().run()

### Paddle ##
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


from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
import game


class Paddle(Widget):
	
	def __init__(self, **kwargs):
		super(Paddle, self).__init__(**kwargs)
		self.pos = kwargs.get("pos")
		self.size = (game.PADDLE_WIDTH, game.PADDLE_HEIGHT)
		self._colour = game.PADDLE_COLOUR
		self._clickable = True
		
		with self.canvas:
			Color(self._colour)
			self.rect = Rectangle(pos=self.pos, size=self.size)
		self.bind(pos=self.redraw, size=self.redraw)
	
	
	def setClickable(self, newstate):
		self._clickable = newstate
	
	
	def on_touch_down(self, touch):
		if self._clickable and self.collide_point(*touch.pos):
			touch.grab(self)
			return True
		return super(Paddle, self).on_touch_down(touch)
	
	
	def on_touch_move(self, touch):
			if touch.grab_current is self:
				touch_y = touch.pos[1]
				new_y = touch_y - (self.size[1] / 2)
				self.pos = (self.pos[0], new_y)
				return True
			return super(Paddle,self).on_touch_move(touch)
	
	
	def on_touch_up(self, touch):
		if touch.grab_current is self:
			touch.ungrab(self)
			return True
		return super(Paddle, self).on_touch_up(touch)
	
	
	def redraw(self, *args):
			self.rect.size = self.size
			self.rect.pos = self.pos
			
			

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
import kivy

from vector2D import Vector2D as V2D



kivy.require(kivy.__version__)

class TestApp(App):
	
	def build(self):
		vect = V2D((300, 400))
		message = "x: {}, y: {}".format(vect.x, vect.y)
		return Label(text=message)


TestApp().run()
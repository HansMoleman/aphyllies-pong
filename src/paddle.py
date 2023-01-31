
### Paddle ##
#
# EXEC:
# DEPN:
#
# This class defines the functionality of the paddle, which are used
# to return the ball to the opponent.
#
# ---
#  ver
# ---
##


from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from pygame.math import Vector2 as V2D
import game



class Paddle(Widget):

    def __init__(self, **kwargs):
        super(Paddle, self).__init__(**kwargs)

        # paddle properties
        self._colour = game.PADDLE_COLOUR
        init_pos = kwargs.get("pos")
        self._pos_vect = V2D(init_pos[0], init_pos[1])
        self._size = game.PADDLE_SIZE
        self._clickable = True

        with self.canvas:
            rgba = self._colour
            Color(rgba[0], rgba[1], rgba[2], rgba[3], mode="rgba")
            self.rect = Rectangle(pos=(self._pos_vect.x, self._pos_vect.y),
                                size=self._size
                            )
    

    def on_touch_move(self, touch):
        if self._clickable:
            newpos = touch.pos
            new_y = newpos[1] - (game.PADDLE_SIZE[1] / 2)
            self._pos_vect.y = new_y
            self.rect.pos = (self._pos_vect.x, self._pos_vect.y)
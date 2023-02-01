
### Ball ##
#
# EXEC:
# DEPN:
#
# This class defines the ball that player hits.
#
# ---
#  ver
# ---
##


from kivy.graphics import Color, Rectangle
from kivy.vector import Vector
from kivy.uix.widget import Widget
import game


class Ball(Widget):

    def __init__(self, **kwargs):
        super(Ball, self).__init__(**kwargs)

        self.pos = (game.BALL_X, game.BALL_Y)
        self.size = (game.BALL_WIDTH, game.BALL_HEIGHT)

        self._direction = Vector(self.pos)
        self._speed = Vector((0, 0))

        with self.canvas:
            Color(game.BALL_COLOUR)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.redraw, size=self.redraw)
    

    def setSpeed(self, newspeed):
        self._speed = Vector(newspeed)


    def redraw(self, *kwargs):
        #self._direction += self._speed
        #self.pos = self._direction
        self.rect.pos = self.pos
    

    def updateState(self, padl_l, padl_r):
        if padl_l.collide_point(self._direction.x, self._direction.y):
            self._speed.x *= -1
        elif padl_l.collide_point(self._direction.x, (self._direction.y + self.size[1])):
            self._speed.x *= -1
        
        '''
        if padl_r.collide_point((self._direction.x + self.size[0]), self._direction.y):
            self._speed.x *= -1
        elif padl_r.collide_point((self._direction.x + self.size[0]), (self._direction.y + self.size[1])):
            self._speed.x *= -1
        '''
        if padl_r.collide_widget(self):
            self._speed.x *= -1

        if self._direction.x <= 0:
            self._speed.x *= -1
        elif (game.WINDOW_WIDTH - self.size[0]) <= self._direction.x:
            self._speed.x *= -1
        
        if self._direction.y <= 0:
            self._speed.y *= -1
        elif (game.WINDOW_HEIGHT - self.size[1]) <= self._direction.y:
            self._speed.y *= -1
        
        self._direction += self._speed
        self.pos = self._direction

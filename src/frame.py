
### Frame ##
#
# EXEC:
# DEPN:
#
# This file implements a frame that can have other widgets added
# to it.
#
# ---
#  ver
# ---
##

from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget



class Frame(Widget):

    def __init__(self, **kwargs):
        super(Frame, self).__init__(**kwargs)

        # frame properties
        self._colour = kwargs.get("colour", (0, 0, 0, 1))
        self._position = kwargs.get("pos")
        self._size = kwargs.get("size")
        self._contents = []

        with self.canvas:
            rgba = self._colour
            Color(rgba[0], rgba[1], rgba[2], rgba[3], mode="rgba")
            self.rect = Rectangle(pos=self._position, size=self._size)

            for widget in self._contents:
                rgba = widget._colour
                Color(rgba[0], rgba[1], rgba[2], rgba[3], mode="rgba")
                widget.rect = Rectangle(pos=widget._pos_vect, size=widget._size)
    

    def addWidget(self, widget):
        self._contents.append(widget)
        self.add_widget(widget)
        
        rgba = widget._colour
        Color(rgba[0], rgba[1], rgba[2], rgba[3], mode="rgba")
        widget.rect = Rectangle(pos=widget._pos_vect, size=widget._size)
    
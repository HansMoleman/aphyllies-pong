
### Vector2D ##
#
# EXEC:
# DEPN:
#
# This class defines a two dimensional vector that
# provides easy access to the x and y components.
#
# ---
#  ver
# ---
##


class Vector2D:
	
	def __init__(self, *args):
		self.x = None
		self.y = None
		
		if type(args[0]) is tuple:
			position = args[0]
			self.x = position[0]
			self.y = position[1]
		else:
			self.x = args[0]
			self.y = args[1]	
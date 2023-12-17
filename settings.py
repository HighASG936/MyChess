
class Settings:
	
	def __init__(self):
		# board settings
		self.tile_size = 92
		self.tile_center = self.tile_size/2
		self.board_n = 8
		self.board_size = self.tile_size * self.board_n
		self.background_color = (255, 255, 255)
		self.tile_colors = [(240, 240, 240), (84, 168, 98)]
		self.marker_color = (0, 179, 255, 80)
		self.bg_color = (225, 225, 225)		
  

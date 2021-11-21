class TextureModel:
	def __init__(self, texture) -> None:
		self.texture = texture

	@property
	def texture(self):
		return self.texture

	@texture.setter
	def setTexture(self, texture):
		self.texture = texture

	@texture.deleter
	def deleteTexture(self):
		del self.texture

class PainterModel:
	def __init__(self, textures={}, textures_map=[]) -> None:
		self.textures = textures
		self.texturesMap = textures_map

		self.observers = []



	# textures
	@property
	def textures(self):
		return self.textures

	@textures.setter
	def setTextures(self, textures):
		self.textures = textures

	@textures.deleter
	def deleteTextures(self):
		del self.textures

	def appendTexture(self, key, texture) -> None:
		self.textures[key] = texture




	# map of textures
	@property
	def texturesMap(self):
		return self.texturesMap

	@texturesMap.setter
	def setTexturesMap(self, texturesMap):
		self.texturesMap = texturesMap

	@texturesMap.deleter
	def deleteTexturesMap(self):
		del self.texturesMap

	def changeTexture(self, x, y, texture):
		self.texturesMap[x][y] = texture


	# observers
	def addObserver(self, observer) -> None:
		self.observers.append(observer)

	def removeObserver(self, observer) -> None:
		self.observers.remove(observer)

	def notifyChanges(self) -> None:
		for observer in self.observers:
			observer.change()

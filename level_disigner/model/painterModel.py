from level_disigner.model.texturesModel import TexturesModel


class PainterModel:
	def __init__(self, textures_map=[]) -> None:
		self.texturesMap = textures_map

		self.observers = []


	# textures
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

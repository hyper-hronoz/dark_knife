import uuid


class TexturesModel:
	def __init__(self, textures={}) -> None:
		self.textures = textures

		self.observers = []

	def addTexture(self, texture) -> None:
		self.textures[str(uuid.uuid4())] = texture
		self.notifyChanges()

	def removeTexture(self, id, texture) -> None:
		del self.textures[id]
		self.notifyChanges()

	def updateTexture(self, id, texture) -> None:
		self.textures[id] = texture
		self.notifyChanges()

	def addObserver(self, observer) -> None:
		self.observers.append(observer)

	def removeObserver(self, observer) -> None:
		self.observers.remove(observer)

	def notifyChanges(self) -> None:
		for observer in self.observers:
			observer.change()

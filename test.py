class Test:
	def __init__(self) -> None:
		self._isLeftPressed = False
		pass

	@property
	def isLeftPressed(self):
		return self._isLeftPressed

	@isLeftPressed.setter
	def isLeftPressed(self, isPressed):
		self._isLeftPressed = isPressed
		self.update()

	def update(self):
		print("Update", self._isLeftPressed)

	
test = Test()
print(test.isLeftPressed)
test.isLeftPressed = True
print(test.isLeftPressed)

	

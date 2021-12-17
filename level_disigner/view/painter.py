import base64
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QEvent, QObject, QRect, Qt
from PyQt5.QtGui import QBrush, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget
from model import TextureModel, TexturesModel, PainterModel
from model import Cell
from utility import MetaObserver, FinalMetaQWidget


class Painter(QWidget, MetaObserver, metaclass=FinalMetaQWidget):
	textureBrash: TextureModel = None 

	XOffset = 0
	YOffset = 0
	isSpacePressed = False
	isLeftMouseButtonPressed = False
	isRightMouseButtonPressed = False

	decodedPictures = {}

	def __init__(self, texturesModel, mapModel, size) -> None:
		self._texturesModel: TexturesModel = texturesModel
		self._mapModel: PainterModel = mapModel
		self._mapModel.addObserver(self)
		self._size = size
		super(Painter, self).__init__()

	def paintEvent(self, event):
		self.painter = QPainter()
		self.painter.begin(self)

		width = self.painter.device().width()
		height = self.painter.device().height()

		height_amount = height // Cell.side 
		width_amount = width // Cell.side 

		if not self._size["height"]:
			self._size["height"] = height_amount
		if not self._size["width"]:
			self._size["width"] = width_amount

		self.margin_horizontal = int((width - (Cell.side * self._size["width"])) / 2)
		self.marging_vertical = int((height - (Cell.side * self._size["height"])) / 2)

		counter = 0
		for y in range(self._size["height"]):
			for x in range(self._size["width"]):
				if (counter >= len(self._mapModel.texturesMap)):
					break
				self._mapModel.texturesMap[counter]["x"] = x * Cell.side + self.margin_horizontal 
				self._mapModel.texturesMap[counter]["y"] = y * Cell.side + self.marging_vertical 
				counter += 1

		if (len(self._mapModel.texturesMap) == 0):
			for y in range(self._size["height"]):
				for x in range(self._size["width"]):
					self._mapModel.texturesMap.append(
						{"x": x * Cell.side + self.margin_horizontal, "y": y * Cell.side + self.marging_vertical, "fill": ""})

		self.drawGrid(self._mapModel.texturesMap)

		self.painter.end()

	def setIsSpacePressed(self, value):
		Painter.isSpacePressed = value

	def drawGrid(self, grid): 
		for cell in grid:
			if (cell["fill"] != "" and Painter.textureBrash != None):
				if (cell["fill"] not in Painter.decodedPictures):
					pixmap = QtGui.QPixmap()
					pixmap.loadFromData(base64.b64decode(self._texturesModel.textures[cell["fill"]].texture))
					Painter.decodedPictures[cell["fill"]] = pixmap
				else:
					pixmap = Painter.decodedPictures[cell["fill"]]
				rect = QRect(cell['x'], cell['y'], Cell.side, Cell.side)
				self.painter.drawPixmap(rect, pixmap)
			else:
				self.painter.setPen(QPen())
				self.painter.setBrush(QBrush())
				self.painter.drawRect(
					cell['x'], cell['y'], Cell.side, Cell.side)

	def getCurrentPosition(self, event) -> dict:
		return {"x": event.x(), "y": event.y()}

	def mousePressEvent(self, event) -> None:
		self.mouseStartPosition = self.getCurrentPosition(event)
		self.previousMousePosition = self.mouseStartPosition

		if event.button() == QtCore.Qt.LeftButton:
			Painter.isLeftMouseButtonPressed = True

		if event.button() == QtCore.Qt.RightButton:
			Painter.isRightMouseButtonPressed = True

		self.drawTextures(event)
		self.deleteTextures(event)

	def movement(self, event):
		if (not Painter.isSpacePressed):
			return
		mouseCurrentPosition = self.getCurrentPosition(event)

		velocity = 1

		if abs(self.mouseStartPosition["x"] - mouseCurrentPosition["x"]) % Cell.side == 0:
			# mouse right drag
			if self.mouseStartPosition["x"] < mouseCurrentPosition["x"] and not Painter.XOffset <= 0:
				Painter.XOffset -= velocity

			# mouse left drag
			if self.mouseStartPosition["x"] > mouseCurrentPosition["x"]:
				Painter.XOffset += velocity

			self.mouseStartPosition["x"] = mouseCurrentPosition["x"]

		if abs(self.mouseStartPosition["y"] - mouseCurrentPosition["y"]) % Cell.side == 0:
			# mouse up drag
			if self.mouseStartPosition["y"] < mouseCurrentPosition["y"] and not Painter.YOffset <= 0:
				Painter.YOffset -= velocity

			# mouse down drag
			if self.mouseStartPosition["y"] > mouseCurrentPosition["y"]:
				Painter.YOffset += velocity

			self.mouseStartPosition["y"] = mouseCurrentPosition["y"]

		self.previousMousePosition = mouseCurrentPosition

	def deleteTextures(self, event):
		if (self.isSpacePressed or (not Painter.isRightMouseButtonPressed)) and Painter.textureBrash != None:
			return

		currentPosition = self.getCurrentPosition(event)
		for i, cell in enumerate(self._mapModel.texturesMap):
			if cell["x"] <= currentPosition["x"] <= cell["x"] + Cell.side and cell["y"] <= currentPosition["y"] <= cell["y"] + Cell.side:
				self._mapModel.texturesMap[i]["fill"] = "" 
				break
		self._mapModel.notifyChanges()

	def drawTextures(self, event):
		if (self.isSpacePressed or (not Painter.isLeftMouseButtonPressed)):
			return
		currentPosition = self.getCurrentPosition(event)

		for i, cell in enumerate(self._mapModel.texturesMap):
			if cell["x"] <= currentPosition["x"] <= cell["x"] + Cell.side and cell["y"] <= currentPosition["y"] <= cell["y"] + Cell.side:
				self._mapModel.texturesMap[i]["fill"] = Painter.textureBrash 
				break
		self._mapModel.notifyChanges()

	def mouseMoveEvent(self, event) -> None:
		self.movement(event)
		self.drawTextures(event)
		self.deleteTextures(event)

	def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
		if event.button() == QtCore.Qt.LeftButton:
			Painter.isLeftMouseButtonPressed = False
		if event.button() == QtCore.Qt.RightButton:
			Painter.isRightMouseButtonPressed = False

	def change(self):
		self.update()

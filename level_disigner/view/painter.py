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

	def __init__(self, texturesModel, mapModel) -> None:
		self._texturesModel: TexturesModel = texturesModel
		self._mapModel: PainterModel = mapModel
		self._mapModel.addObserver(self)
		super(Painter, self).__init__()

	def paintEvent(self, event):
		# print("updating")
		self.painter = QPainter()
		self.painter.begin(self)

		if (len(self._mapModel.texturesMap) == 0):

			width = self.painter.device().width()
			height = self.painter.device().height()

			height_amount = height // Cell.side + 1
			width_amount = width // Cell.side + 1
			for y in range(height_amount):
				for x in range(width_amount):
					self._mapModel.texturesMap.append(
						{"x": x * Cell.side, "y": y * Cell.side, "fill": ""})

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

		print(Painter.XOffset, Painter.YOffset)

	def deleteTextures(self, event):
		if (self.isSpacePressed or (not Painter.isRightMouseButtonPressed)):
			return
		currentPosition = self.getCurrentPosition(event)
		for i, cell in enumerate(self._mapModel.texturesMap):
			if (currentPosition["x"] // Cell.side) * Cell.side == cell["x"] and (currentPosition["y"] // Cell.side) * Cell.side == cell["y"] and self._mapModel.texturesMap[i]["fill"] == 1:
				self._mapModel.texturesMap[i]["fill"] = "" 
				break
		self._mapModel.notifyChanges()

	def drawTextures(self, event):
		if (self.isSpacePressed or (not Painter.isLeftMouseButtonPressed)):
			return
		currentPosition = self.getCurrentPosition(event)
		for i, cell in enumerate(self._mapModel.texturesMap):
			if (currentPosition["x"] // Cell.side) * Cell.side == cell["x"] and (currentPosition["y"] // Cell.side) * Cell.side == cell["y"] and self._mapModel.texturesMap[i]["fill"] != 1 and Painter.textureBrash != None:
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

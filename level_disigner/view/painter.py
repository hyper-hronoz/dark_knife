from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLineEdit, QWidget
from model import Cell


class Painter(QWidget):
	XOffset = 0
	YOffset = 0

	def __init__(self) -> None:
		super(Painter, self).__init__()

	def paintEvent(self, event):
		self.painter = QPainter()
		self.painter.begin(self)

		width = self.painter.device().width()
		height = self.painter.device().height()

		height_amount = height // Cell.side + 1
		width_amount = width // Cell.side + 1

		_grid = []

		for y in range(height_amount):
			for x in range(width_amount):
				_grid.append({"x": x * Cell.side, "y": y * Cell.side})

		self.drawGrid(_grid)

		self.painter.end()

	def drawGrid(self, grid):
		for cell in grid:
			self.painter.drawRect(cell['x'], cell['y'], Cell.side, Cell.side)

	def getCurrentPosition(self, event) -> dict:
		return {"x": event.x(), "y": event.y()}

	# def event(self, event: QtCore.QEvent) -> bool:
	# 	print(event)
	# 	if (event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Space):
	# 		print("space")
	# 		return True
	# 	return super().event(event)
	# def keyPressEvent(self, event) -> None:
	# 	print(event)

	def mousePressEvent(self, event) -> None:
		print(event.x(), event.y())
		self.mouseStartPosition = self.getCurrentPosition(event)
		self.previousMousePosition = self.mouseStartPosition

	def mouseMoveEvent(self, event) -> None:
		mouseCurrentPosition = self.getCurrentPosition(event)

		velocity = 1

		if abs(self.mouseStartPosition["x"] - mouseCurrentPosition["x"]) % Cell.side == 0 :
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


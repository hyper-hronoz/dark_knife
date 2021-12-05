from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget
from model import Cell


class Painter(QWidget):

	def __init__(self) -> None:
		super(Painter, self).__init__()

	def paintEvent(self, event):
		self.painter = QPainter()
		self.painter.begin(self)

		width = self.painter.device().width()
		height = self.painter.device().height()

		height_amount = height // Cell.side + 1
		width_amount = width // Cell.side + 1

		for y in range(height_amount):
			for x in range(width_amount):
				self.painter.drawRect(
					x * Cell.side, y * Cell.side, Cell.side, Cell.side)

		self.painter.end()

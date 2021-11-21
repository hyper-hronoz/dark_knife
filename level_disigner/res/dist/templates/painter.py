from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


class Painter(QWidget):

	def __init__(self) -> None:
		super(Painter, self).__init__()

	def paintEvent(self, event):
		self.painter = QPainter()
		self.painter.begin(self)
		self.painter.drawText(100,100, str(event))
		print(str(event))
		self.painter.end()

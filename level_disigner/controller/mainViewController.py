from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QFrame
from view import MainView, Painter
from model import TextureModel, TexturesModel, PainterModel
import json

import os
import base64


class MainViewController():
	def __init__(self):
		self.texturesModel = TexturesModel()
		self.painterModel = PainterModel()

		self.mView = MainView(self, self.texturesModel)

		self._createCanvas()

		self.mView.show()
	
	def _createCanvas(self):
		self._chartilo = Painter(self.texturesModel, self.painterModel)
		self.mView.pasteCanvas(self._chartilo)
		
	def saveFileAs(self):
		content = {"textures": []}
		for texture in self.texturesModel.__dict__["textures"]:
			content["textures"].append({texture : self.texturesModel.__dict__["textures"][texture].__dict__["texture"]})
		content["texturesMap"] = self.painterModel.__dict__["texturesMap"]

		options = QFileDialog.Options()
		fileName, _ = QFileDialog.getSaveFileName(self.mView,"QFileDialog.getSaveFileName()","hyi","All Files (*);;Text Files (*.hyi)", options=options)
		if fileName:
			file = open(fileName,'w')
			file.write(str(content))
			file.close()
	
	def setPainterBrash(self, obj, event):
		if isinstance(obj, QFrame) and event.type() == QtCore.QEvent.MouseButtonPress:
			Painter.textureBrash = obj.objectName()

	def onSpacePressed(self, event):
		if event.isAutoRepeat():
			return
		if event.key()==QtCore.Qt.Key_Space:
			self._chartilo.setIsSpacePressed(True)

	def onSpaceReleased(self, event):
		if event.isAutoRepeat():
			return
		if event.key()==QtCore.Qt.Key_Space:
			self._chartilo.setIsSpacePressed(False)

	def addNewTexture(self):
		fname = QFileDialog.getOpenFileName(self.mView, 'Выбрать картинку ', '', "(*.jpg *.png *.jpeg, *.JPEG *.JPG, *.PNG)")[0]
		if not fname:
			return
		head, tail = os.path.split(fname)
		with open(fname, "rb") as image2string:
			converted_string = base64.b64encode(image2string.read())

			texture = TextureModel(converted_string, tail)

			self.texturesModel.addTexture(texture)



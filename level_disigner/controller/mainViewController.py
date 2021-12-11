from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QFrame
from view import MainView
from model import TextureModel, TexturesModel

import os
import base64


class MainViewController():
	def __init__(self):
		self.texturesModel = TexturesModel()

		self.mView = MainView(self, self.texturesModel)

		self.mView.show()

	def selectTexture(self, obj, event):
		if isinstance(obj, QFrame) and event.type() == QtCore.QEvent.MouseButtonPress:
			_model = self._model.textures

	def addNewTexture(self):
		fname = QFileDialog.getOpenFileName(self.mView, 'Выбрать картинку ', '', "(*.jpg *.png *.jpeg, *.JPEG *.JPG, *.PNG)")[0]
		if not fname:
			return
		head, tail = os.path.split(fname)
		with open(fname, "rb") as image2string:
			converted_string = base64.b64encode(image2string.read())

			texture = TextureModel(converted_string, tail)

			self.texturesModel.addTexture(texture)



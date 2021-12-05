from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QBoxLayout, QFrame, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget
from res import Ui_MainWindow as Template
from .painter import Painter
from utility import MetaObserver, FinalMeta

import base64
from time import sleep

class MainView(QMainWindow, MetaObserver, metaclass=FinalMeta):

    def __init__(self, controller, model):
        super(MainView, self).__init__()
        self.template = Template()
        self.template.setupUi(self)
        self.showMaximized()
        self.createCanvas()

        self._model = model
        self._model.addObserver(self)

        self.template.header_add_button.clicked.connect(controller.addNewTexture)

    def createCanvas(self):
        self._chartilo = Painter()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._chartilo)
        self.template.grid_frame.setLayout(layout)

    def updateCanvas(self):
        self._chartilo.updateCanvas()

    def setCanvasData(self, data):
        self._chartilo.setData(data)

    def setCanvasStates(self, states):
        self._chartilo.setStates(states)

    def change(self):
        _model = self._model.textures

        for i in reversed(range(self.template.textures_frame.layout().count())): 
            self.template.textures_frame.layout().itemAt(i).widget().setParent(None)

        for id in _model:

            frame = QFrame()
            frame.setObjectName(str(id))
            layout = QHBoxLayout()
            widget = QWidget()
            image = QLabel(widget)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(base64.b64decode(_model[id].texture))
            image.setPixmap(pixmap.scaled(50, 50))
            image.setBaseSize
            layout.addWidget(image)
            layout.addWidget(QLabel(_model[id].name))
            frame.setLayout(layout)

            widget.show()


            self.template.textures_frame.layout().addWidget(frame)


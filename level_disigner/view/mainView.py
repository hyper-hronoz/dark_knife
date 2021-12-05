from PyQt5.QtWidgets import QApplication, QBoxLayout, QMainWindow, QVBoxLayout, QWidget
from res import Ui_MainWindow as Template
from .painter import Painter
from utility import MetaObserver, FinalMeta

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
        print(self._model)

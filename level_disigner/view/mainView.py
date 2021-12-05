from PyQt5.QtWidgets import QApplication, QBoxLayout, QMainWindow, QVBoxLayout, QWidget
from res import Ui_MainWindow as Template
from res import Painter

class MainView(QMainWindow):

    def __init__(self):
        super(MainView, self).__init__()
        self.template = Template()
        self.template.setupUi(self)
        self.showMaximized()
        self.createCanvas()

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
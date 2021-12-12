from abc import ABCMeta
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from utility import MetaObserver


class FinalMetaMainWindow(type(QMainWindow), type(MetaObserver)):
    pass

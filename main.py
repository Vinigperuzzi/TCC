from PySide6.QtWidgets import QApplication, QMainWindow
from src.gui.PPP_interface import Ui_MainWindow
from src.python.ButtonsAction import ButtonsAction
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("PPP Debugger")
    ButtonsAction.set_base_buttons(mainWindow)
    mainWindow.show()
    #mainWindow.showMaximized()
    app.exec()
from PySide6.QtWidgets import QApplication, QMainWindow
from src.gui.ui5 import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QFileDialog, QLabel

class Controller:

    FILE_TYPES = "*.c"

    @staticmethod
    def load_file(window):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(window, "Select File", "", Controller.FILE_TYPES, options=options)
        if file_path:
            print(f"Arquivo selecionado: {file_path}")
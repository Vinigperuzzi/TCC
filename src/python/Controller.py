from PySide6.QtWidgets import QLineEdit, QFileDialog, QDialog, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Slot
import subprocess

class Controller:

    FILE_TYPES = "*.c"

    @staticmethod
    def load_file(window):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(window, "Select File", "", Controller.FILE_TYPES, options=options)
        if file_path:
            try:    
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                    window.my_code_editor.setPlainText(file_content)
                    Controller.save_file(window)
                    Controller.build_file(window)
                    file.close()
                    window.statusbar.showMessage("File loaded successfully")
            except Exception as e:
                window.statusbar.showMessage("Error loading file")

    @staticmethod
    def save_file(window):
        content = window.my_code_editor.toPlainText()
        if content == "":
            window.statusbar.showMessage("Empty code")
            return
        
        try:
            with open("code.c", "w", encoding="utf-8") as file:
                file.write(content)
                window.statusbar.showMessage("File saved successfully")
        except Exception as e:
            window.statusbar.showMessage("File couldn't be saved")

    @staticmethod
    def build_file(window):
        Controller.__show_build_modal(window)

    def __show_build_modal(window):
        modal = QDialog()
        modal.setWindowTitle("Set compilation flags")
        modal.setGeometry(400, 300, 300, 100)

        info_label = QLabel()
        info_label.setText("-lpthread -fopenmp are set by default\nKeep empty if none other are required")

        text_input = QLineEdit(modal)
        text_input.setPlaceholderText("-lm -shared...")

        submit_button = QPushButton("Submit", modal)
        submit_button.clicked.connect(Controller.__submit_flags(text_input, modal, window))

        layout = QVBoxLayout()
        layout.addWidget(info_label)
        layout.addWidget(text_input)
        layout.addWidget(submit_button)
        modal.setLayout(layout)
        modal.exec()

    @Slot()
    def __submit_flags(text, modal, window):
        def inner():
            modal.accept()
            command = ["gcc", "-g", "-o", "code", "code.c", "-lpthread", "-fopenmp"]
            response = subprocess.run(command, capture_output=True, text=True)
            if response.returncode == 0:
                window.statusbar.showMessage("File build successfully named code")
            else:
                window.statusbar.showMessage("Error building file")
        return inner
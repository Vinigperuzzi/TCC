from PySide6.QtWidgets import QLineEdit, QFileDialog, QDialog, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Slot
from src.python.GDBMI_Controller import GDBMI_Controller
import subprocess

class Controller:
    FILE_TYPES = "*.c"
    gdbmi = GDBMI_Controller()

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
        GDBMI_Controller.update_expressions_list(Controller.gdbmi, window)

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
                Controller.gdbmi.load_file()
            else:
                window.statusbar.showMessage("Error building file")
        return inner
    
    @staticmethod
    def set_breakpoint_manually(window):
        Controller.__show_bp_man_modal(window)

    def __show_bp_man_modal(window):
        modal = QDialog()
        modal.setWindowTitle("Inform the line or the name of function to insert breakpoint")
        modal.setGeometry(400, 300, 300, 100)

        text_input = QLineEdit(modal)
        text_input.setPlaceholderText("1, 2, 15, main...")

        submit_button = QPushButton("Submit", modal)
        submit_button.clicked.connect(Controller.__submit_bp_manual(text_input, modal, window))

        layout = QVBoxLayout()
        layout.addWidget(text_input)
        layout.addWidget(submit_button)
        modal.setLayout(layout)
        modal.exec()

    @Slot()
    def __submit_bp_manual(text, modal, window):
        def inner():
            modal.accept()
            Controller.gdbmi.set_bp_manually(text.text(), window)
        return inner
    
    @staticmethod
    def remove_all_bkpt(window):
        Controller.gdbmi.remove_all_bkpts(window)

    @staticmethod
    def set_breakpoint(window):
        Controller.gdbmi.set_breakpoint(window)

    @staticmethod
    def remove_breakpoint(window):
        Controller.gdbmi.remove_breakpoint(window)

    @staticmethod
    def send_exec(window, action):
        Controller.gdbmi.send_exec(window, action)

    @staticmethod
    def inspect(window):
        field = window.my_inspect_text
        text = field.text()
        field.setText("")
        Controller.gdbmi.inspect(window, text)

    @staticmethod
    def remove_all_expressions(window):
        Controller.gdbmi.remove_all_expressions(window, True)

    @staticmethod
    def set_expression_manually(window):
        Controller.__show_exp_man_modal(window)

    def __show_exp_man_modal(window):
        modal = QDialog()
        modal.setWindowTitle("Inform the expression to be added to inspector")
        modal.setGeometry(400, 300, 300, 100)

        text_input = QLineEdit(modal)
        text_input.setPlaceholderText("test, id, i, j...")

        submit_button = QPushButton("Submit", modal)
        submit_button.clicked.connect(Controller.__submit_exp_manual(text_input, modal, window))

        layout = QVBoxLayout()
        layout.addWidget(text_input)
        layout.addWidget(submit_button)
        modal.setLayout(layout)
        modal.exec()

    @Slot()
    def __submit_exp_manual(text, modal, window):
        def inner():
            modal.accept()
            Controller.gdbmi.inspect(window, text.text())
        return inner

    @staticmethod
    def terminal(text):
        Controller.gdbmi.terminal(text)
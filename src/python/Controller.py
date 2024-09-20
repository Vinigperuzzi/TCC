from PySide6.QtWidgets import QMainWindow, QLineEdit, QFileDialog, QDialog, QPushButton, QVBoxLayout, QWidget, QLabel, QTextBrowser
from PySide6.QtCore import Slot
from src.python.GDBMI_Controller import GDBMI_Controller
import subprocess
from pathlib import Path
from src.gui.PPP_commands import Ui_Form as UI_Command
from src.gui.PPP_controls import Ui_Form as UI_Control

class Controller:
    FILE_TYPES = "*.c"
    no_gdb = None
    try:
        gdbmi = GDBMI_Controller()
    except:
        no_gdb = True

    @staticmethod
    def check_GDB(window):
        if Controller.no_gdb:
            window.my_code_editor.setPlainText("\n\n\t\t\tALERT: There's is no GDB installed on this system, please, note that GDB must be installed in order to run this application")
            window.my_output_terminal.setText("Error: GDB not installed, failed to connect to GDB")
            window.statusbar.showMessage("Error trying to connect to GDB")
            return False
        return True

    @staticmethod
    def new(window):
        Controller.gdbmi.new(window)

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
        modal.setWindowTitle("Inform the breakpoint position")
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
    def manipulate_threads(window, lock):
        Controller.gdbmi.manipulate_threads(window, lock)

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
        Controller.__show_exp_man_modal(window, "add")

    @staticmethod
    def remove_expression_manually(window):
        Controller.__show_exp_man_modal(window, "remove")

    def __show_exp_man_modal(window, type):
        modal = QDialog()
        if type == "add":
            modal.setWindowTitle("Inform the expression to be added to inspector")
        else:
             modal.setWindowTitle("Inform the expression to be removed inspector")

        modal.setGeometry(400, 300, 300, 100)

        text_input = QLineEdit(modal)
        text_input.setPlaceholderText("test, id, i, j...")

        submit_button = QPushButton("Submit", modal)
        if type == "add":
            submit_button.clicked.connect(Controller.__submit_exp_manual(text_input, modal, window))
        else:
            submit_button.clicked.connect(Controller.__remove_exp_manual(text_input, modal, window))

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
    
    @Slot()
    def __remove_exp_manual(text, modal, window):
        def inner():
            modal.accept()
            Controller.gdbmi.remove_one_expression(window, text.text())
        return inner
    
    @staticmethod
    def assembly(window):
        Controller.gdbmi.advanced_info(window, "assembly")

    def registers(window):
        Controller.gdbmi.advanced_info(window, "registers")


    @staticmethod
    def terminal(window):
        Controller.__show_terminal_modal(window)

    def __show_terminal_modal(window):
        modal = QMainWindow(window)
        modal.setWindowTitle("Terminal")

        modal.setGeometry(400, 300, 300, 100)

        central_widget = QWidget(modal)
        modal.setCentralWidget(central_widget)

        info_label = QLabel("Inform the command to be executed\n"
                            "A list of commands can be found at help menu\n"
                            "NOTE: please, consider that certain commands may brake the graphic interface because it overrides somes UI's features")

        text_input = QLineEdit(modal)
        text_input.setPlaceholderText("-thread-info, -thread-select <ID>, -stack-select-frame <FRAME_NUMBER>...")

        submit_button = QPushButton("Submit", modal)
        submit_button.clicked.connect(Controller.__submit_command(text_input, modal, window))

        layout = QVBoxLayout()
        layout.addWidget(info_label)
        layout.addWidget(text_input)
        layout.addWidget(submit_button)
        central_widget.setLayout(layout)
        modal.show()

    @Slot()
    def __submit_command(text, modal, window):
        def inner():
            Controller.gdbmi.terminal(window, text.text())
            text.setText("")
        return inner

    @staticmethod
    def remove_all_th_buttons(window):
        Controller.gdbmi.remove_all_th_buttons(window)

    @staticmethod
    def show_help_command(window):
        class CommandWindow(QWidget, UI_Command):
            def __init__(self, parent=None):
                super().__init__(parent)
                self.setupUi(self)
                self.setWindowTitle("GDBMI commands")
                self.closeButton.clicked.connect(self.close)

        command = CommandWindow(window)
        command.show()

    @staticmethod
    def show_help_control(window):
        class ControlWindow(QWidget, UI_Control):
            def __init__(self, parent=None):
                super().__init__(parent)
                self.setupUi(self)
                self.setWindowTitle("PPP Debugger controls")
                self.closeButton.clicked.connect(self.close)

        control = ControlWindow(window)
        control.show()

    @staticmethod
    def show_text_modal(window, type):
        modal = QMainWindow(window)
        if type == 'about':
            modal.setWindowTitle("About")
        else:
            modal.setWindowTitle("Documentation")
        modal.setGeometry(200, 300, 500, 300)

        central_widget = QWidget(modal)
        modal.setCentralWidget(central_widget)
        project_root = Path(__file__).parent.parent
        if type == 'about':
            txt_path = project_root / 'txt' / 'about.txt'
        else:
            txt_path = project_root / 'txt' / 'doc.txt'
        with open(txt_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
        info_text = QTextBrowser()
        info_text.setPlainText(file_content)

        layout = QVBoxLayout()
        layout.addWidget(info_text)
        central_widget.setLayout(layout)
        modal.show()
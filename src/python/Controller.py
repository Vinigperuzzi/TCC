from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QFileDialog, QLabel

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
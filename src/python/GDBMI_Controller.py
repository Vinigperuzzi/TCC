from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLabel, QPushButton, QMainWindow, QWidget, QTextBrowser, QVBoxLayout
from pygdbmi.gdbcontroller import GdbController
from src.python.View import View
import json
from pprint import pprint
from io import StringIO
import subprocess

class GDBMI_Controller:
    def __init__(self):
        self.conn = GdbController()
        self.last_line = None
        self.expressions_list = []

    def new(self, window):
        self.remove_all_th_buttons(window)
        self.remove_all_expressions(window, True)
        text = window.my_output_terminal
        text.setText("")
        self.remove_all_bkpts(window)

        window.my_code_editor.setPlainText("")
        cursor = window.my_code_editor.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        cursor.select(QTextCursor.SelectionType.LineUnderCursor)
        format = QTextCharFormat()
        format.setBackground(QColor("transparent"))

        self.conn.write("kill")

    def load_file(self):
        self.conn.write("-file-exec-and-symbols code")


    def set_breakpoint(self, window):
        line = GDBMI_Controller.__get_line_number(window)
        line_number = int(line)
        GDBMI_Controller.__set_breakpoint(self, line_number, window)


    def remove_breakpoint(self, window):
        line = GDBMI_Controller.__get_line_number(window)
        bkpts_list = GDBMI_Controller.__get_lines_by_number_bkpts(self)
        bkpt = bkpts_list[line]
        response = self.conn.write(f"-break-delete {bkpt}")
        if response[0]['message'] == "done":
            window.statusbar.showMessage(f"Breakpoint deleted from line {line}")
            View.delete_breakpoint(window, line)
        else:
            window.statusbar.showMessage(f"Error while trying to delete breakpoint at line {line}")

    def set_bp_manually(self, text, window):
        GDBMI_Controller.__set_breakpoint(self, text, window)

    def remove_all_bkpts(self, window):
        try:
            qtd_bkpts = GDBMI_Controller.__get_bkpts_qtd(self)
            if qtd_bkpts > 0:
                for i in range(1, qtd_bkpts+1):
                    self.conn.write(f"-break-delete {i}")
                window.statusbar.showMessage("All breakpoints removed")
                View.delete_breakpoints(window)
                return
            window.statusbar.showMessage("There's no breakpoint to be removed")
        except Exception as e:
            window.statusbar.showMessage("An error occurred while trying to remove breakpoints, maybe there's no builded file")

    def send_exec(gdbmi, window, param):
        gdbmi.conn.write(f"-exec-{param}")
        GDBMI_Controller.__update_bkpt_line(gdbmi, window)
        GDBMI_Controller.update_expressions_list(gdbmi, window)
        window.statusbar.showMessage(f"Debugging moving on with {param}")
        current_thread = gdbmi.__update_threads(window)
        gdbmi.change_thread(current_thread, window)()

    def manipulate_threads(gdbmi, window, lock):
        label = window.my_controlling
        status_bar = window.statusbar
        if lock == 'on':
            gdbmi.conn.write("set scheduler-locking on")
            label.setText("Controlling: Selected")
            status_bar.showMessage("Controlling only the selected thread with the execution commands")
        else:
            gdbmi.conn.write("set scheduler-locking off")
            label.setText("Controlling: ALL")
            status_bar.showMessage("Controlling all threads with the execution commands")


    def __update_threads(gdbmi, window):
        gdbmi.remove_all_th_buttons(window)
        response = gdbmi.conn.write("-thread-list-ids")
        current_thread = gdbmi.__update_threads_terminal(window, response)
        th_list = response[0]['payload']['thread-ids']['thread-id']
        gdbmi.add_th_buttons(window, th_list)
        return current_thread

    def __update_threads_terminal(gdbmi, window, response):
        th_qtd = int(response[0]['payload']['number-of-threads'])
        current_thread = int(response[0]['payload']['current-thread-id'])
        text = window.my_output_terminal
        text.setText(f"Showing the scope of the thread number: {current_thread}\nNumber of current active threads: {th_qtd}")
        return current_thread
        
    def remove_all_th_buttons(gdbmi, window):
        layout = window.my_thread_list.layout()
        while layout.count() > 0:
            item = layout.takeAt(0)

            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


    def add_th_buttons(gdbmi, window, th_list):
        layout = window.my_thread_list.layout()
        for th in th_list:
            button = QPushButton(th)
            layout.addWidget(button)
            button.clicked.connect(gdbmi.change_thread(int(th), window))
    

    @Slot()
    def change_thread(self, thread_id, window):
        def inner():
            self.conn.write(f"-thread-select {thread_id}")
            response = self.conn.write("-thread-list-ids")
            self.__update_threads_terminal(window, response)
            self.update_expressions_list(window)
            self.__update_bkpt_line(window)
        return inner


    def inspect(gdbmi, window, text):
        elements = text.split()

        if len(elements) == 1:
            if text not in gdbmi.expressions_list:
                gdbmi.expressions_list.append(text)
                GDBMI_Controller.update_expressions_list(gdbmi, window)
                window.statusbar.showMessage(f"Added expression {text} to inspector")
            window.statusbar.showMessage(f"Expression {text} are already in inspector")
        elif len(elements) == 3 and elements[1] == "=" and elements[0] in gdbmi.expressions_list:
            gdbmi.conn.write(f"set var {elements[0]} = {elements[2]}")
            GDBMI_Controller.update_expressions_list(gdbmi, window)
            window.statusbar.showMessage(f"Change the value of expression {elements[0]}")
        else:
            window.statusbar.showMessage("Wrong syntax, try again")
        

    def update_expressions_list(gdbmi, window):
        GDBMI_Controller.remove_all_expressions(gdbmi, window)
        for text in gdbmi.expressions_list:
            response = gdbmi.conn.write(f"-data-evaluate-expression {text}")
            try:
                value = response[0]['payload']['value']

            except Exception as e:
                value = "No data"

            finally:
                label = QLabel(f"{text}: {value}")
                layout = window.my_data_inspector.layout()
                layout.addWidget(label)

    def remove_one_expression(gdbmi, window, exp):
        if exp in gdbmi.expressions_list:
            gdbmi.expressions_list.remove(exp)
            GDBMI_Controller.update_expressions_list(gdbmi, window)
            window.statusbar.showMessage(f"removed expression {exp} to inspector")
        window.statusbar.showMessage(f"There's no expression {exp} to be removed")

    def remove_all_expressions(gdbmi, window, from_list=False):
        layout = window.my_data_inspector.layout()
        while layout.count() > 0:
            item = layout.takeAt(0)

            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        if from_list:
            gdbmi.expressions_list.clear()
            window.statusbar.showMessage(f"all expressions removed")


    def advanced_info(gdbmi, window, type):
        if type == "assembly":
            response = gdbmi.conn.write("disassemble")
        else:
            response = gdbmi.conn.write("info registers")

        modal = QMainWindow(window)
        if type == "assembly":
            modal.setWindowTitle("Assembly Code")
        else:
            modal.setWindowTitle("Registers Information")
        
        modal.setGeometry(200, 300, 800, 400)

        central_widget = QWidget(modal)
        modal.setCentralWidget(central_widget)

        info_text = QTextBrowser()
        for res in response:
            info_text.append(f"{res['payload']}\n")

        layout = QVBoxLayout()
        layout.addWidget(info_text)
        central_widget.setLayout(layout)
        modal.show()

    def terminal(gdbmi, window, text):
        response = gdbmi.conn.write(text)
        text = window.my_output_terminal
        buffer = StringIO()
        pprint(response, stream=buffer)
        terminal_text = buffer.getvalue()
        text.setText(terminal_text)
        gdbmi.update_expressions_list(window)


    def __update_bkpt_line(gdbmi, window):
        response = gdbmi.conn.write("-stack-info-frame")
        line = int(response[0]['payload']['frame']['line'])
        View.return_line_pattern(window, gdbmi.last_line)
        View.update_breakpoints(window, GDBMI_Controller.__get_bkpts_list(gdbmi))
        gdbmi.last_line = line
        View.stop_line(window, line)

    def __get_bkpts_qtd(gdbmi):
        response = gdbmi.conn.write("-break-list")
        qtd_bkpts = response[0]['payload']['BreakpointTable']['nr_rows']
        return int(qtd_bkpts)
    
    def __get_bkpts_list(gdbmi):
        response = gdbmi.conn.write("-break-list")
        array = []
        for i in range(GDBMI_Controller.__get_bkpts_qtd(gdbmi)):
            value = response[0]['payload']['BreakpointTable']['body'][i]['line']
            array.append(int(value))
        return array
    
    def __get_lines_by_number_bkpts(gdbmi):
        response = gdbmi.conn.write("-break-list")
        array = {}
        for i in range(GDBMI_Controller.__get_bkpts_qtd(gdbmi)):
            line = int(response[0]['payload']['BreakpointTable']['body'][i]['line'])
            number = int(response[0]['payload']['BreakpointTable']['body'][i]['number'])
            array[line] = number
        return array
    
    def __get_line_number(window):
        cursor = window.my_code_editor.textCursor()
        return cursor.blockNumber() + 1
    
    def __set_breakpoint(gdbmi, line, window):
        gdb_response = gdbmi.conn.write(f"-break-insert {line}")
        if gdb_response[0]['message'] == "done":
            window.statusbar.showMessage(f"Breakpoint insertion at line {gdb_response[0]['payload']['bkpt']['line']}")
            View.update_breakpoints(window, GDBMI_Controller.__get_bkpts_list(gdbmi))
        else:
            window.statusbar.showMessage(f"Breakpoint not inserted: {gdb_response[0]['payload']['msg']}")

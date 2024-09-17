from PySide6.QtGui import QTextCursor
from pygdbmi.gdbcontroller import GdbController
from src.python.View import View
import json
from pprint import pprint

class GDBMI_Controller:
    def __init__(self):
        self.conn = GdbController()

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
        response = gdbmi.conn.write(param)
        #print(f"resposta = \n {response}\n\n\n")
        pprint(response)
        print(f"\n\n\n\n\n")
        try:
            terminal = gdbmi.conn.get_gdb_response()
            print(f"terminal = {terminal}\n\n\n")
        except Exception as e:
            print(f"Num deu {e}")

    def terminal(gdbmi, text):
        response = gdbmi.conn.write(text)
        print(response)


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
from pygdbmi.gdbcontroller import GdbController
from src.python.View import View
import json

class GDBMI_Controller:
    def __init__(self):
        self.conn = GdbController()

    def load_file(self):
        gdb_response = self.conn.write("-file-exec-and-symbols code")

    def set_bp_manually(self, text, window):
        gdb_response = self.conn.write(f"-break-insert {text}")
        if gdb_response[0]['message'] == "done":
            window.statusbar.showMessage(f"Breakpoint insertion at line {gdb_response[0]['payload']['bkpt']['line']}")
            View.update_breakpoints(window, GDBMI_Controller.__get_bkpts_list(self))
        else:
            window.statusbar.showMessage(f"Breakpoint not inserted: {gdb_response[0]['payload']['msg']}")

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
from pygdbmi.gdbcontroller import GdbController
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
        else:
            window.statusbar.showMessage(f"Breakpoint not inserted: {gdb_response[0]['payload']['msg']}")
        #bp_list = self.conn.write("-break-list")
        #print("list: ", bp_list)
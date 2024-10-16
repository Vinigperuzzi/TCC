from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QShortcut, QKeySequence
from src.python.Controller import Controller

class ButtonsAction:
    window = None
    @staticmethod
    def set_base_buttons(main_window):
        ButtonsAction.window = main_window
        has_GDB = Controller.check_GDB(main_window)
        ButtonsAction.__connect_menu_bar()
        ButtonsAction.__connect_br_buttons()
        ButtonsAction.__connect_control_buttons()
        ButtonsAction.__connect_controlling_buttons()
        ButtonsAction.__connect_inspect_button()
        ButtonsAction.__add_shortcuts()
        if has_GDB:
            Controller.remove_all_th_buttons(main_window)

    def __connect_menu_bar():
        ButtonsAction.__connect_menu_file()
        ButtonsAction.__connect_menu_control()
        ButtonsAction.__connect_menu_breakpoints()
        ButtonsAction.__connect_menu_data_inspector()
        ButtonsAction.__connect_menu_view()
        ButtonsAction.__connect_menu_terminal()
        ButtonsAction.__connect_menu_help()

    def __connect_br_buttons():
        ButtonsAction.window.my_button_add_br.clicked.connect(ButtonsAction.__add)
        ButtonsAction.window.my_button_rm_br.clicked.connect(ButtonsAction.__remove)

    def __connect_control_buttons():
        ButtonsAction.window.my_button_run.clicked.connect(ButtonsAction.__run)
        ButtonsAction.window.my_button_next.clicked.connect(ButtonsAction.__next)
        ButtonsAction.window.my_button_continue.clicked.connect(ButtonsAction.__continue)
        ButtonsAction.window.my_button_step_in.clicked.connect(ButtonsAction.__step)
        ButtonsAction.window.my_button_finish.clicked.connect(ButtonsAction.__finish)

    def __connect_controlling_buttons():
        ButtonsAction.window.my_all_threads.clicked.connect(ButtonsAction.__all_threads)
        ButtonsAction.window.my_selected_thread.clicked.connect(ButtonsAction.__selected_thread)

    def __connect_inspect_button():
        ButtonsAction.window.my_button_inspect.clicked.connect(ButtonsAction.__inspect)
        ButtonsAction.window.my_change_value.clicked.connect(ButtonsAction.__inspect)
        ButtonsAction.window.my_inspect_text.setPlaceholderText("expression, expression = value...")

    def __connect_menu_file():
        ButtonsAction.window.actionNew.triggered.connect(ButtonsAction.__new)
        ButtonsAction.window.actionLoad.triggered.connect(ButtonsAction.__load)
        ButtonsAction.window.actionSave.triggered.connect(ButtonsAction.__save)
        ButtonsAction.window.actionBuild.triggered.connect(ButtonsAction.__build)

    def __connect_menu_control():
        ButtonsAction.window.actionRun_R.triggered.connect(ButtonsAction.__run)
        ButtonsAction.window.actionNext_2.triggered.connect(ButtonsAction.__next)
        ButtonsAction.window.actionContinue_1.triggered.connect(ButtonsAction.__continue)
        ButtonsAction.window.actionStep_In_F.triggered.connect(ButtonsAction.__step)
        ButtonsAction.window.actionFinish_F9.triggered.connect(ButtonsAction.__finish)

    def __connect_menu_breakpoints():
        ButtonsAction.window.actionAdd_breakpoint_to_line.triggered.connect(ButtonsAction.__add)
        ButtonsAction.window.actionInform_breakpoint_position.triggered.connect(ButtonsAction.__add_2)
        ButtonsAction.window.actionRemove_all_breakpoints.triggered.connect(ButtonsAction.__remove_all)
        ButtonsAction.window.actionRemove_breakpoint_from_selected_line.triggered.connect(ButtonsAction.__remove)

    def __connect_menu_data_inspector():
        ButtonsAction.window.actionInsert_expression.triggered.connect(ButtonsAction.__exp_insert)
        ButtonsAction.window.actionRemove_expression.triggered.connect(ButtonsAction.__exp_remove)
        ButtonsAction.window.actionClear_expression_list.triggered.connect(ButtonsAction.__exp_remove_all)

    def __connect_menu_view():
        ButtonsAction.window.actionAssembly_Code.triggered.connect(ButtonsAction.__assembly)
        ButtonsAction.window.actionRegister_List.triggered.connect(ButtonsAction.__registers)

    def __connect_menu_terminal():
        ButtonsAction.window.actionNew_Terminal.triggered.connect(ButtonsAction.__terminal)

    def __connect_menu_help():
        ButtonsAction.window.actionAbout.triggered.connect(ButtonsAction.__about)
        ButtonsAction.window.actionCommands.triggered.connect(ButtonsAction.__commands)
        ButtonsAction.window.actionControls.triggered.connect(ButtonsAction.__controls)
        ButtonsAction.window.actionDocumentation.triggered.connect(ButtonsAction.__documentation)

    #Actions
    #File
    def __new():
        Controller.new(ButtonsAction.window)

    def __load():
        Controller.load_file(ButtonsAction.window)

    def __save():
        Controller.save_file(ButtonsAction.window)

    def __build():
        Controller.build_file(ButtonsAction.window)

    #Control
    def __run():
        Controller.send_exec(ButtonsAction.window, "run")

    def __next():
        Controller.send_exec(ButtonsAction.window, "next")

    def __continue():
        Controller.send_exec(ButtonsAction.window, "continue")

    def __step():
        Controller.send_exec(ButtonsAction.window, "step")

    def __finish():
        Controller.send_exec(ButtonsAction.window, "finish")

    #breakpoints
    def __add():
        Controller.set_breakpoint(ButtonsAction.window)

    def __remove():
        Controller.remove_breakpoint(ButtonsAction.window)

    def __add_2():
        Controller.set_breakpoint_manually(ButtonsAction.window)

    def __remove_all():
        Controller.remove_all_bkpt(ButtonsAction.window)

    #data inspector
    def __exp_insert():
        Controller.set_expression_manually(ButtonsAction.window)

    def __exp_remove():
        Controller.remove_expression_manually(ButtonsAction.window)

    def __exp_remove_all():
        Controller.remove_all_expressions(ButtonsAction.window)

    #view
    def __assembly():
        Controller.assembly(ButtonsAction.window)

    def __registers():
        Controller.registers(ButtonsAction.window)

    #terminal
    def __terminal():
        Controller.terminal(ButtonsAction.window)

    #help
    def __commands():
        Controller.show_help_command(ButtonsAction.window)

    def __controls():
        Controller.show_help_control(ButtonsAction.window)
    
    def __about():
        Controller.show_text_modal(ButtonsAction.window, 'about')

    def __documentation():
        Controller.show_text_modal(ButtonsAction.window, 'documentation')

    def __inspect():
        Controller.inspect(ButtonsAction.window)

    def __all_threads():
        Controller.manipulate_threads(ButtonsAction.window, "off")

    def __selected_thread():
        Controller.manipulate_threads(ButtonsAction.window, "on")

    def __add_shortcuts():
        QShortcut(QKeySequence(Qt.Key_F1), ButtonsAction.window).activated.connect(ButtonsAction.__run)
        QShortcut(QKeySequence(Qt.Key_F5), ButtonsAction.window).activated.connect(ButtonsAction.__continue)
        QShortcut(QKeySequence(Qt.Key_F6), ButtonsAction.window).activated.connect(ButtonsAction.__next)
        QShortcut(QKeySequence(Qt.Key_F7), ButtonsAction.window).activated.connect(ButtonsAction.__step)
        QShortcut(QKeySequence(Qt.Key_F9), ButtonsAction.window).activated.connect(ButtonsAction.__finish)
        QShortcut(QKeySequence(Qt.CTRL | Qt.Key_S), ButtonsAction.window).activated.connect(ButtonsAction.__save)
        QShortcut(QKeySequence(Qt.CTRL | Qt.Key_B), ButtonsAction.window).activated.connect(ButtonsAction.__build)
        QShortcut(QKeySequence(Qt.CTRL | Qt.Key_L), ButtonsAction.window).activated.connect(ButtonsAction.__load)
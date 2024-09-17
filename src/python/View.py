from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor

class View:
    bkpts = []

    @staticmethod
    def update_breakpoints(window, bkpts):
        View.bkpts = bkpts
        cursor = window.my_code_editor.textCursor()
        for bkpt in bkpts:
            cursor.movePosition(QTextCursor.MoveOperation.Start)
            for _ in range(bkpt-1):
                cursor.movePosition(QTextCursor.MoveOperation.Down)

            cursor.select(QTextCursor.SelectionType.LineUnderCursor)

            format = QTextCharFormat()
            format.setBackground(QColor("#248a71"))

            cursor.mergeCharFormat(format)

            window.my_code_editor.update()

    @staticmethod
    def delete_breakpoints(window):
        cursor = window.my_code_editor.textCursor()
        for bkpt in View.bkpts:
            cursor.movePosition(QTextCursor.MoveOperation.Start)
            for _ in range(bkpt-1):
                cursor.movePosition(QTextCursor.MoveOperation.Down)

            View.__set_transparency(cursor, window)

    @staticmethod
    def delete_breakpoint(window, line):
        cursor = window.my_code_editor.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        for _ in range(line-1):
            cursor.movePosition(QTextCursor.MoveOperation.Down)
        
        View.__set_transparency(cursor, window)

    def __set_transparency(cursor, window):
        cursor.select(QTextCursor.SelectionType.LineUnderCursor)

        format = QTextCharFormat()
        format.setBackground(QColor("transparent"))

        cursor.mergeCharFormat(format)

        window.my_code_editor.update()
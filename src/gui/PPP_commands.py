# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PPP_commands.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QScrollArea, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        Form.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(15, 61, 83);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1260, 700))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.closeButton = QPushButton(self.scrollAreaWidgetContents)
        self.closeButton.setObjectName(u"closeButton")

        self.verticalLayout_2.addWidget(self.closeButton)

        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.closeButton.setText(QCoreApplication.translate("Form", u"Close Window", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -exec-run:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Starts program execution from the defined entry point (usually main). If the program is already running, it will be continued.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\""
                        " font-size:12pt; color:#f44536;\">\u2022 -exec-continue:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Continues program execution from where it is currently paused.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -exec-next:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Executes the next line of code, skipping over function calls.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -exec-step:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Executes the next line of code, but steps into called functions.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022"
                        " -exec-finish:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Continues execution until exiting the current function.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -exec-until LOCATION:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Continues execution until the program reaches a specific line or function (defined by LOCATION).<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -break-insert LOCATION:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Inserts a breakpoint at the specified location (can be a line, function, etc.).<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;"
                        " color:#f44536;\">\u2022 -break-delete BREAKPOINT_NUMBER:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Removes a breakpoint specified by its number.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -break-disable BREAKPOINT_NUMBER:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Disables a breakpoint without removing it.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -break-enable BREAKPOINT_NUMBER:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Reactivates a disabled breakpoint.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -break-list:</span><"
                        "span style=\" font-size:12pt; color:#00fcd2;\"> Lists all currently defined breakpoints.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -data-evaluate-expression EXPRESSION:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Evaluates the specified expression (e.g., the value of a variable) in the current context and returns the result.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -data-list-register-values FORMAT:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Lists the values of the processor's registers. The FORMAT can be binary, decimal, hexadecimal, etc.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" font-size:12pt; color:#f44536;\">\u2022 -stack-list-arguments PRINT_VALUES START END:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Lists the function arguments in the stack trace. PRINT_VALUES can be 0 (do not show values) or 1 (show values). START and END specify the range of frames to display.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -thread-info:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Displays information about all threads currently running in the program.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -thread-select THREAD_ID:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Selects the execution thread specified by THREAD_ID.<br /></span></p>\n"
"<p style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -thread-list-ids:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Lists the IDs of all threads in the program.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -thread-exit THREAD_ID:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Forces the specified thread to exit.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -thread-stop:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Stops the execution of all threads.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -stack-info-depth:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Returns the depth of the stack, i.e., the number of frames in the stack trace.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -stack-list-frames:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Lists all frames (functions and call locations) in the current stack.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -stack-select-frame FRAME_NUMBER: </span><span style=\" font-size:12pt; color:#00fcd2;\">Selects a specific frame in the stack, allowing inspection of that frame's state.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -data-read-memory START_ADDR FORMAT WORD_SIZE NUM_WORDS:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Reads memory content from a specific address. FORMAT defines the output format (hexadecimal, decimal, etc.), and WORD_SIZE defines the size of the words to be read.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -data-write-memory START_ADDR VALUE FORMAT:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Writes a value to memory at a specific address.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -exec-interrupt:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Interrupts the program's execution"
                        " (equivalent to Ctrl+C in the GDB terminal).<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -exec-kill:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Immediately terminates the debugged process.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -break-watch EXPRESSION:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Inserts a watchpoint, a conditional </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#00fcd2;\">breakpoint triggered when the value of the specified expression changes.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -break-watch-access EXPRESSION:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Inserts a watchpoint triggered when the expression is accessed (read or written).<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -break-watch-delete WATCHPOINT_NUMBER:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Removes a specified watchpoint.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -break-condition BREAKPOINT_NUMBER EXPRESSION:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Defines a condition for a breakpoint. The breakpoint will only be triggered if the EXPRESSION evaluates to true.<br /></span></p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -file-exec-and-symbols FILENAME:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Loads the executable file and its debug symbols.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -file-symbol-file FILENAME:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Loads only the debug symbols from a specific file.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -var-create NAME FRAME EXPR:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Creates a new watched variable based on the specified expression (EXPR) and returns an identifier.<br /"
                        "></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -var-delete NAME:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Removes a watched variable specified by NAME.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -var-evaluate-expression NAME:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Evaluates the expression of a watched variable and returns the value.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -var-list-children NAME:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Lists the children (sub-variables) of a watched variable (useful for complex struct"
                        "ures like arrays or structs).<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -inferior-info:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Displays information about the processes (inferiors) that GDB is controlling. This is useful when debugging programs with multiple processes.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -inferior-select ID:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Selects the process (inferior) with the specified ID for debugging.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -target-attach PROCESS_ID:</span><span style=\""
                        " font-size:12pt; color:#00fcd2;\"> Attaches the debugger to a running process specified by its process ID.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -target-detach:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Detaches the debugger from the current process.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -gdb-show VARIABLE:</span><span style=\" font-size:12pt; color:#00fcd2;\"> Displays the value of an internal GDB variable (e.g., print elements to show how many elements are displayed by default in arrays).<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 -"
                        "gdb-set VARIABLE VALUE: </span><span style=\" font-size:12pt; color:#00fcd2;\">Sets the value of an internal GDB variable.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; color:#00fcd2;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 NOTE: </span><span style=\" font-size:12pt; color:#00fcd2;\">Depending on the version of GDB, some commands may not be available.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f44536;\">\u2022 NOTE 2: </span><span style=\" font-size:12pt; color:#00fcd2;\">All GDB commands work on the interface terminal as well.</span></p></body></html>", None))
    # retranslateUi


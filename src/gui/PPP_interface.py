# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PPP_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(15, 61, 83);\n"
"}\n"
"\n"
"QFrame {\n"
"	border-style:none;\n"
"}\n"
"\n"
"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionBuild = QAction(MainWindow)
        self.actionBuild.setObjectName(u"actionBuild")
        self.actionRun_R = QAction(MainWindow)
        self.actionRun_R.setObjectName(u"actionRun_R")
        self.actionContinue_1 = QAction(MainWindow)
        self.actionContinue_1.setObjectName(u"actionContinue_1")
        self.actionNext_2 = QAction(MainWindow)
        self.actionNext_2.setObjectName(u"actionNext_2")
        self.actionStep_In_F = QAction(MainWindow)
        self.actionStep_In_F.setObjectName(u"actionStep_In_F")
        self.actionFinish_F9 = QAction(MainWindow)
        self.actionFinish_F9.setObjectName(u"actionFinish_F9")
        self.actionAssembly_Code = QAction(MainWindow)
        self.actionAssembly_Code.setObjectName(u"actionAssembly_Code")
        self.actionRegister_List = QAction(MainWindow)
        self.actionRegister_List.setObjectName(u"actionRegister_List")
        self.actionNew_Terminal = QAction(MainWindow)
        self.actionNew_Terminal.setObjectName(u"actionNew_Terminal")
        self.actionCommands = QAction(MainWindow)
        self.actionCommands.setObjectName(u"actionCommands")
        self.actionControls = QAction(MainWindow)
        self.actionControls.setObjectName(u"actionControls")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionInsert_expression = QAction(MainWindow)
        self.actionInsert_expression.setObjectName(u"actionInsert_expression")
        self.actionRemove_expression = QAction(MainWindow)
        self.actionRemove_expression.setObjectName(u"actionRemove_expression")
        self.actionClear_expression_list = QAction(MainWindow)
        self.actionClear_expression_list.setObjectName(u"actionClear_expression_list")
        self.actionAdd_breakpoint_to_line = QAction(MainWindow)
        self.actionAdd_breakpoint_to_line.setObjectName(u"actionAdd_breakpoint_to_line")
        self.actionRemove_breakpoint_from_selected_line = QAction(MainWindow)
        self.actionRemove_breakpoint_from_selected_line.setObjectName(u"actionRemove_breakpoint_from_selected_line")
        self.actionInform_breakpoint_position = QAction(MainWindow)
        self.actionInform_breakpoint_position.setObjectName(u"actionInform_breakpoint_position")
        self.actionRemove_all_breakpoints = QAction(MainWindow)
        self.actionRemove_all_breakpoints.setObjectName(u"actionRemove_all_breakpoints")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(18)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QTextEdit {\n"
"	border-width: 2px;\n"
"    border-style: solid;\n"
"	border-color:rgb(0, 252, 210);\n"
"    border-radius: 6px;\n"
"	background-color: rgb(9, 36, 48);\n"
"	font-size: 14px;\n"
"	color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(0, 30, 25);\n"
"	color:rgb(0, 252, 210);\n"
"	border-width: 1px;\n"
"    border-style: solid;\n"
"	border-color:rgb(0, 30, 25);\n"
"    border-radius: 4px;\n"
"	border-bottom: 2px solid black;\n"
"	border-right: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(0, 15, 12);\n"
"	color:rgb(0, 103, 86);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:black;\n"
"	color:rgb(0, 90, 75);\n"
"	margin-top:4px;\n"
"}\n"
"\n"
"QFrame {\n"
"	border-width: 1px;\n"
"    border-style: solid;\n"
"	border-color:rgb(0, 252, 210);\n"
"    border-radius: 4px;\n"
"	background-color:rgb(20, 81, 109);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(4)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.my_button_add_br = QPushButton(self.frame_4)
        self.my_button_add_br.setObjectName(u"my_button_add_br")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.my_button_add_br.sizePolicy().hasHeightForWidth())
        self.my_button_add_br.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.my_button_add_br)

        self.my_button_rm_br = QPushButton(self.frame_4)
        self.my_button_rm_br.setObjectName(u"my_button_rm_br")
        sizePolicy3.setHeightForWidth(self.my_button_rm_br.sizePolicy().hasHeightForWidth())
        self.my_button_rm_br.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.my_button_rm_br)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.control_panel = QFrame(self.frame_3)
        self.control_panel.setObjectName(u"control_panel")
        sizePolicy2.setHeightForWidth(self.control_panel.sizePolicy().hasHeightForWidth())
        self.control_panel.setSizePolicy(sizePolicy2)
        self.control_panel.setStyleSheet(u"")
        self.control_panel.setFrameShape(QFrame.StyledPanel)
        self.control_panel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.control_panel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.my_button_run = QPushButton(self.control_panel)
        self.my_button_run.setObjectName(u"my_button_run")
        sizePolicy3.setHeightForWidth(self.my_button_run.sizePolicy().hasHeightForWidth())
        self.my_button_run.setSizePolicy(sizePolicy3)
        self.my_button_run.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.my_button_run)

        self.my_button_continue = QPushButton(self.control_panel)
        self.my_button_continue.setObjectName(u"my_button_continue")
        sizePolicy3.setHeightForWidth(self.my_button_continue.sizePolicy().hasHeightForWidth())
        self.my_button_continue.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.my_button_continue)

        self.my_button_next = QPushButton(self.control_panel)
        self.my_button_next.setObjectName(u"my_button_next")
        sizePolicy3.setHeightForWidth(self.my_button_next.sizePolicy().hasHeightForWidth())
        self.my_button_next.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.my_button_next)

        self.my_button_step_in = QPushButton(self.control_panel)
        self.my_button_step_in.setObjectName(u"my_button_step_in")
        sizePolicy3.setHeightForWidth(self.my_button_step_in.sizePolicy().hasHeightForWidth())
        self.my_button_step_in.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.my_button_step_in)

        self.my_button_finish = QPushButton(self.control_panel)
        self.my_button_finish.setObjectName(u"my_button_finish")
        sizePolicy3.setHeightForWidth(self.my_button_finish.sizePolicy().hasHeightForWidth())
        self.my_button_finish.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.my_button_finish)


        self.horizontalLayout_2.addWidget(self.control_panel)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setStyleSheet(u"border-style: none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_7)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(4)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	background-color:rgb(0, 30, 25);\n"
"}\n"
"\n"
"QTextBrowser {\n"
"	background-color:rgb(0, 30, 25);\n"
"	color:white;\n"
"	margin-left:15px;\n"
"	border-style:none;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.my_output_terminal = QTextBrowser(self.frame_5)
        self.my_output_terminal.setObjectName(u"my_output_terminal")

        self.verticalLayout_3.addWidget(self.my_output_terminal)


        self.gridLayout_3.addWidget(self.frame_5, 2, 0, 1, 1)

        self.my_code_editor = QTextEdit(self.frame)
        self.my_code_editor.setObjectName(u"my_code_editor")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(13)
        sizePolicy5.setHeightForWidth(self.my_code_editor.sizePolicy().hasHeightForWidth())
        self.my_code_editor.setSizePolicy(sizePolicy5)
        font = QFont()
        self.my_code_editor.setFont(font)
        self.my_code_editor.setStyleSheet(u"")
        self.my_code_editor.setTabStopDistance(40.000000000000000)

        self.gridLayout_3.addWidget(self.my_code_editor, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(10)
        sizePolicy7.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy7)
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	background-color:rgb(20, 81, 109);\n"
"}\n"
"\n"
"QLabel {\n"
"	max-height: 40px;\n"
"	min-height: 30px;\n"
"	color:rgb(70, 0, 5);\n"
"	qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QScrollArea {\n"
"	border-width: 2px;\n"
"    border-style: solid;\n"
"	border-color:rgb(0, 252, 210);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color:rgb(20, 81, 109);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color:rgb(0, 30, 25);\n"
"	color:rgb(0, 252, 210);\n"
"	border-width: 1px;\n"
"    border-style: solid;\n"
"	border-color:rgb(0, 30, 25);\n"
"    border-radius: 4px;\n"
"	border-bottom: 2px solid black;\n"
"	border-right: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(0, 15, 12);\n"
"	color:rgb(0, 103, 86);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:black;\n"
"	color:rgb(0, 90, 75);\n"
"	margin-top:4px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color:rgb(70, 0, 5);\n"
"	background-color:rgb(40, 164, 222);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(3)
        sizePolicy8.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy8)
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy9)
        self.label.setStyleSheet(u"color:white;\n"
"font-size: 16px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.my_inspect_text = QLineEdit(self.frame_9)
        self.my_inspect_text.setObjectName(u"my_inspect_text")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.my_inspect_text.sizePolicy().hasHeightForWidth())
        self.my_inspect_text.setSizePolicy(sizePolicy10)

        self.verticalLayout_6.addWidget(self.my_inspect_text)

        self.my_button_inspect = QPushButton(self.frame_9)
        self.my_button_inspect.setObjectName(u"my_button_inspect")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.my_button_inspect.sizePolicy().hasHeightForWidth())
        self.my_button_inspect.setSizePolicy(sizePolicy11)

        self.verticalLayout_6.addWidget(self.my_button_inspect)

        self.scrollArea = QScrollArea(self.frame_9)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.my_data_inspector = QWidget()
        self.my_data_inspector.setObjectName(u"my_data_inspector")
        self.my_data_inspector.setGeometry(QRect(0, 0, 215, 245))
        self.verticalLayout_7 = QVBoxLayout(self.my_data_inspector)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea.setWidget(self.my_data_inspector)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(7)
        sizePolicy12.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy12)
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color:rgb(20, 81, 109);\n"
"}\n"
"\n"
"QLabel {\n"
"	max-height: 40px;\n"
"	min-height: 30px;\n"
"	color:rgb(70, 0, 5);\n"
"	qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QScrollArea {\n"
"	border-width: 2px;\n"
"    border-style: solid;\n"
"	border-color:rgb(0, 252, 210);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color:rgb(20, 81, 109);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(70, 0, 5);\n"
"	color:rgb(0, 252, 210);\n"
"	border-width: 1px;\n"
"    border-style: solid;\n"
"	border-color:rgb(0, 30, 25);\n"
"    border-radius: 4px;\n"
"	border-bottom: 2px solid black;\n"
"	border-right: 2px solid black;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(0, 15, 12);\n"
"	color:rgb(0, 103, 86);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:black;\n"
"	color:rgb(0, 90, 75);\n"
"	margin-top:4px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy4.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy4)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: white;\n"
"font-size:16px;")

        self.verticalLayout_9.addWidget(self.label_10)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.thread_scroll = QScrollArea(self.frame_8)
        self.thread_scroll.setObjectName(u"thread_scroll")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(21)
        sizePolicy13.setHeightForWidth(self.thread_scroll.sizePolicy().hasHeightForWidth())
        self.thread_scroll.setSizePolicy(sizePolicy13)
        self.thread_scroll.setStyleSheet(u"")
        self.thread_scroll.setWidgetResizable(True)
        self.my_thread_list = QWidget()
        self.my_thread_list.setObjectName(u"my_thread_list")
        self.my_thread_list.setGeometry(QRect(0, 0, 216, 324))
        self.gridLayout = QGridLayout(self.my_thread_list)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_10 = QPushButton(self.my_thread_list)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 1, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.my_thread_list)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout.addWidget(self.pushButton_17, 3, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.my_thread_list)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 3, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.my_thread_list)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 1, 2, 1, 1)

        self.pushButton_23 = QPushButton(self.my_thread_list)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout.addWidget(self.pushButton_23, 6, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.my_thread_list)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 2, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.my_thread_list)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout.addWidget(self.pushButton_19, 4, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.my_thread_list)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 2, 1, 1, 1)

        self.pushButton_22 = QPushButton(self.my_thread_list)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout.addWidget(self.pushButton_22, 5, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.my_thread_list)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.my_thread_list)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 0, 2, 1, 1)

        self.pushButton_21 = QPushButton(self.my_thread_list)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout.addWidget(self.pushButton_21, 4, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.my_thread_list)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.my_thread_list)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout.addWidget(self.pushButton_16, 2, 2, 1, 1)

        self.pushButton_20 = QPushButton(self.my_thread_list)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout.addWidget(self.pushButton_20, 4, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.my_thread_list)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout.addWidget(self.pushButton_18, 3, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.my_thread_list)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_24 = QPushButton(self.my_thread_list)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout.addWidget(self.pushButton_24, 7, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.my_thread_list)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout.addWidget(self.pushButton_25, 5, 1, 1, 1)

        self.pushButton_26 = QPushButton(self.my_thread_list)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout.addWidget(self.pushButton_26, 5, 2, 1, 1)

        self.pushButton_27 = QPushButton(self.my_thread_list)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.gridLayout.addWidget(self.pushButton_27, 6, 1, 1, 1)

        self.pushButton_28 = QPushButton(self.my_thread_list)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout.addWidget(self.pushButton_28, 6, 2, 1, 1)

        self.pushButton_29 = QPushButton(self.my_thread_list)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.gridLayout.addWidget(self.pushButton_29, 7, 1, 1, 1)

        self.pushButton_30 = QPushButton(self.my_thread_list)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout.addWidget(self.pushButton_30, 7, 2, 1, 1)

        self.thread_scroll.setWidget(self.my_thread_list)

        self.verticalLayout_8.addWidget(self.thread_scroll)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        self.menubar.setStyleSheet(u"QMenuBar::item {\n"
"	background-color:rgb(15, 61, 83);\n"
"	color:rgb(0, 252, 210);\n"
"}\n"
"\n"
"QMenuBar::item:hover {\n"
"	background-color:rgb(0, 132, 110);\n"
"	color:rgb(0, 90, 75);\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"	background-color:rgb(0, 132, 110);\n"
"	color:rgb(0, 90, 75);\n"
"}\n"
"\n"
"QMenu::item {\n"
"	background-color:rgb(15, 61, 83);\n"
"	color:rgb(0, 252, 210);\n"
"}\n"
"\n"
"QMenu::item:hover {\n"
"	background-color:rgb(0, 132, 110);\n"
"	color:rgb(0, 90, 75);\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"	background-color:rgb(0, 132, 110);\n"
"	color:rgb(0, 90, 75);\n"
"}")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuControl = QMenu(self.menubar)
        self.menuControl.setObjectName(u"menuControl")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuTerminal = QMenu(self.menubar)
        self.menuTerminal.setObjectName(u"menuTerminal")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuData_Inspector = QMenu(self.menubar)
        self.menuData_Inspector.setObjectName(u"menuData_Inspector")
        self.menuBreakpoints = QMenu(self.menubar)
        self.menuBreakpoints.setObjectName(u"menuBreakpoints")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color:rgb(0, 252, 210);")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuBreakpoints.menuAction())
        self.menubar.addAction(self.menuData_Inspector.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTerminal.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionBuild)
        self.menuControl.addAction(self.actionRun_R)
        self.menuControl.addAction(self.actionContinue_1)
        self.menuControl.addAction(self.actionNext_2)
        self.menuControl.addAction(self.actionStep_In_F)
        self.menuControl.addAction(self.actionFinish_F9)
        self.menuView.addAction(self.actionAssembly_Code)
        self.menuView.addAction(self.actionRegister_List)
        self.menuTerminal.addAction(self.actionNew_Terminal)
        self.menuHelp.addAction(self.actionCommands)
        self.menuHelp.addAction(self.actionControls)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuData_Inspector.addAction(self.actionInsert_expression)
        self.menuData_Inspector.addAction(self.actionRemove_expression)
        self.menuData_Inspector.addAction(self.actionClear_expression_list)
        self.menuBreakpoints.addAction(self.actionAdd_breakpoint_to_line)
        self.menuBreakpoints.addAction(self.actionRemove_breakpoint_from_selected_line)
        self.menuBreakpoints.addAction(self.actionInform_breakpoint_position)
        self.menuBreakpoints.addAction(self.actionRemove_all_breakpoints)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load (CRTL + L)", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save (CRTL + S)", None))
        self.actionBuild.setText(QCoreApplication.translate("MainWindow", u"Build (CRTL + B)", None))
        self.actionRun_R.setText(QCoreApplication.translate("MainWindow", u"Run (F1)", None))
        self.actionContinue_1.setText(QCoreApplication.translate("MainWindow", u"Continue (F5)", None))
        self.actionNext_2.setText(QCoreApplication.translate("MainWindow", u"Next (F6)", None))
        self.actionStep_In_F.setText(QCoreApplication.translate("MainWindow", u"Step-In (F7)", None))
        self.actionFinish_F9.setText(QCoreApplication.translate("MainWindow", u"Finish (F9)", None))
        self.actionAssembly_Code.setText(QCoreApplication.translate("MainWindow", u"Assembly Code", None))
        self.actionRegister_List.setText(QCoreApplication.translate("MainWindow", u"Register List", None))
        self.actionNew_Terminal.setText(QCoreApplication.translate("MainWindow", u"New Terminal", None))
        self.actionCommands.setText(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.actionControls.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionInsert_expression.setText(QCoreApplication.translate("MainWindow", u"Insert expression", None))
        self.actionRemove_expression.setText(QCoreApplication.translate("MainWindow", u"Remove expression", None))
        self.actionClear_expression_list.setText(QCoreApplication.translate("MainWindow", u"Clear expression list", None))
        self.actionAdd_breakpoint_to_line.setText(QCoreApplication.translate("MainWindow", u"Add breakpoint to selected line", None))
        self.actionRemove_breakpoint_from_selected_line.setText(QCoreApplication.translate("MainWindow", u"Remove breakpoint from current line", None))
        self.actionInform_breakpoint_position.setText(QCoreApplication.translate("MainWindow", u"Inform breakpoint position", None))
        self.actionRemove_all_breakpoints.setText(QCoreApplication.translate("MainWindow", u"Remove all breakpoints", None))
        self.my_button_add_br.setText(QCoreApplication.translate("MainWindow", u"Add Breakpoint", None))
        self.my_button_rm_br.setText(QCoreApplication.translate("MainWindow", u"Remove Breakpoint", None))
        self.my_button_run.setText(QCoreApplication.translate("MainWindow", u"Run (F1)", None))
        self.my_button_continue.setText(QCoreApplication.translate("MainWindow", u"Continue (F5)", None))
        self.my_button_next.setText(QCoreApplication.translate("MainWindow", u"Next (F6)", None))
        self.my_button_step_in.setText(QCoreApplication.translate("MainWindow", u"Step_in (F7)", None))
        self.my_button_finish.setText(QCoreApplication.translate("MainWindow", u"Finish (F9)", None))
        self.my_output_terminal.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.my_code_editor.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Inspector", None))
        self.my_inspect_text.setText("")
        self.my_button_inspect.setText(QCoreApplication.translate("MainWindow", u"Inspect", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Thread List", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuControl.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTerminal.setTitle(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuData_Inspector.setTitle(QCoreApplication.translate("MainWindow", u"Data Inspector", None))
        self.menuBreakpoints.setTitle(QCoreApplication.translate("MainWindow", u"Breakpoints", None))
    # retranslateUi


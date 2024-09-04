# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PPP-MainInterface.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 894)
        MainWindow.setMinimumSize(QSize(1366, 600))
        MainWindow.setStyleSheet(u"background-color:rgb(15, 61, 83);\n"
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
        self.actionContinue_A = QAction(MainWindow)
        self.actionContinue_A.setObjectName(u"actionContinue_A")
        self.actionNext_N = QAction(MainWindow)
        self.actionNext_N.setObjectName(u"actionNext_N")
        self.actionFinish_F = QAction(MainWindow)
        self.actionFinish_F.setObjectName(u"actionFinish_F")
        self.actionAssembly_Code = QAction(MainWindow)
        self.actionAssembly_Code.setObjectName(u"actionAssembly_Code")
        self.actionRegisters_List = QAction(MainWindow)
        self.actionRegisters_List.setObjectName(u"actionRegisters_List")
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QGroupBox {\n"
"	background-color:rgb(15, 61, 83);\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 2px;\n"
"	border-color:rgb(0, 252, 210);\n"
"}\n"
"\n"
"QScrollArea {\n"
"	border-style: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"}")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 160, 271, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color:rgb(20, 81, 109);\n"
"color:rgb(0, 252, 210);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 269, 549))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(280, 60, 551, 651))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"background-color:rgb(8, 33, 44);\n"
"color:rgb(0, 252, 210);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 549, 649))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(839, 280, 271, 431))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.verticalLayoutWidget_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"background-color:rgb(20, 81, 109);\n"
"color:rgb(0, 252, 210);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 269, 429))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.scrollArea_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-2, 715, 1111, 141))
        self.label.setStyleSheet(u"background-color:rgb(0, 30, 25)")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(330, 0, 411, 51))
        self.groupBox.setStyleSheet(u"background-color:rgb(0, 30, 25);\n"
"color:rgb(0, 252, 210);")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 20, 98, 25))
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 20, 97, 25))
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(110, 20, 98, 25))
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(310, 20, 98, 25))
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 60, 271, 91))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(20, 81, 109);\n"
"color:rgb(0, 252, 210);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 30, 251, 41))
        self.label_3.setStyleSheet(u"font-size: 35px;")

        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(840, 60, 271, 201))
        self.frame_2.setStyleSheet(u"background-color:rgb(20, 81, 109);\n"
"color:rgb(0, 252, 210);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 241, 41))
        self.label_4.setStyleSheet(u"font-size: 28px;")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 140, 171, 25))
        self.pushButton.setStyleSheet(u"background-color:rgb(0, 30, 25);\n"
"color:rgb(0, 252, 210);")
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 80, 241, 41))
        self.textEdit.setStyleSheet(u"background-color:rgb(0, 30, 25);\n"
"color:rgb(0, 252, 210);\n"
"font-size:20px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 22))
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
"}")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setStyleSheet(u"QMenu::item {\n"
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
        self.menuControl = QMenu(self.menubar)
        self.menuControl.setObjectName(u"menuControl")
        self.menuControl.setStyleSheet(u"QMenu::item {\n"
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
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuView.setStyleSheet(u"QMenu::item {\n"
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
        self.menuTerminal = QMenu(self.menubar)
        self.menuTerminal.setObjectName(u"menuTerminal")
        self.menuTerminal.setStyleSheet(u"QMenu::item {\n"
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
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setStyleSheet(u"QMenu::item {\n"
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color:rgb(0, 252, 210)")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTerminal.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionBuild)
        self.menuControl.addAction(self.actionRun_R)
        self.menuControl.addAction(self.actionContinue_A)
        self.menuControl.addAction(self.actionNext_N)
        self.menuControl.addAction(self.actionFinish_F)
        self.menuView.addAction(self.actionAssembly_Code)
        self.menuView.addAction(self.actionRegisters_List)
        self.menuTerminal.addAction(self.actionNew_Terminal)
        self.menuHelp.addAction(self.actionCommands)
        self.menuHelp.addAction(self.actionControls)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New                      ", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load                      ", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save                      ", None))
        self.actionBuild.setText(QCoreApplication.translate("MainWindow", u"Build                     ", None))
        self.actionRun_R.setText(QCoreApplication.translate("MainWindow", u"Run (R)                             ", None))
        self.actionContinue_A.setText(QCoreApplication.translate("MainWindow", u"Continue (SPACE BAR)  ", None))
        self.actionNext_N.setText(QCoreApplication.translate("MainWindow", u"Next (N)                           ", None))
        self.actionFinish_F.setText(QCoreApplication.translate("MainWindow", u"Finish (F)                          ", None))
        self.actionAssembly_Code.setText(QCoreApplication.translate("MainWindow", u"Assembly Code ", None))
        self.actionRegisters_List.setText(QCoreApplication.translate("MainWindow", u"Registers List      ", None))
        self.actionNew_Terminal.setText(QCoreApplication.translate("MainWindow", u"New Terminal  ", None))
        self.actionCommands.setText(QCoreApplication.translate("MainWindow", u"Commands          ", None))
        self.actionControls.setText(QCoreApplication.translate("MainWindow", u"Controls                ", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About                    ", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation    ", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"List Of Threads", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"List of Expressions", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Inspect Expression", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuControl.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTerminal.setTitle(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(18)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
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

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.control_panel = QFrame(self.frame_3)
        self.control_panel.setObjectName(u"control_panel")
        sizePolicy2.setHeightForWidth(self.control_panel.sizePolicy().hasHeightForWidth())
        self.control_panel.setSizePolicy(sizePolicy2)
        self.control_panel.setStyleSheet(u"QPushButton {\n"
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
"	background-color:rgb(112, 0, 0);\n"
"	border-width: 1px;\n"
"    border-style: solid;\n"
"	border-color:rgb(0, 252, 210);\n"
"    border-radius: 4px;\n"
"	background-color:rgb(20, 81, 109);\n"
"}")
        self.control_panel.setFrameShape(QFrame.StyledPanel)
        self.control_panel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.control_panel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.control_panel)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.control_panel)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.control_panel)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.control_panel)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.control_panel)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy3.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addWidget(self.control_panel)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_3)

        self.code_frame = QFrame(self.frame)
        self.code_frame.setObjectName(u"code_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(13)
        sizePolicy4.setHeightForWidth(self.code_frame.sizePolicy().hasHeightForWidth())
        self.code_frame.setSizePolicy(sizePolicy4)
        self.code_frame.setFrameShape(QFrame.StyledPanel)
        self.code_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.code_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addWidget(self.code_frame)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(4)
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
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
        self.textBrowser = QTextBrowser(self.frame_5)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_3.addWidget(self.textBrowser)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setStyleSheet(u"background-color:blue;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color:rgb(0, 252, 210);")
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionBuild.setText(QCoreApplication.translate("MainWindow", u"Build", None))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Run (F1)", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Continue (F5)", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Next (F6)", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Step_in (F7)", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Finish (F9)", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00c9 esse aqui</p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuControl.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTerminal.setTitle(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


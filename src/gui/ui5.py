# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1278, 720)
        MainWindow.setMinimumSize(QSize(0, 0))
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
        self.verticalLayoutWidget.setGeometry(QRect(1000, 540, 271, 121))
        self.horizontalLayout = QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color:rgb(20, 81, 109);\n"
"color:rgb(0, 252, 210);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 252, 184))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_5)

        self.pushButton_10 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"background-color:rgb(112, 0, 0);")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color:rgb(112, 0, 0);")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color:rgb(112, 0, 0);")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"background-color:rgb(112, 0, 0);")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"background-color:rgb(112, 0, 0);")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 60, 981, 471))
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 962, 780))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_7 = QCheckBox(self.frame_3)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.horizontalLayout_4.addWidget(self.checkBox_7)

        self.lineEdit_7 = QLineEdit(self.frame_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_4.addWidget(self.lineEdit_7)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_8 = QCheckBox(self.frame_4)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.horizontalLayout_5.addWidget(self.checkBox_8)

        self.lineEdit_8 = QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_5.addWidget(self.lineEdit_8)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_9 = QCheckBox(self.frame_5)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.horizontalLayout_6.addWidget(self.checkBox_9)

        self.lineEdit_9 = QLineEdit(self.frame_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_6.addWidget(self.lineEdit_9)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox_14 = QCheckBox(self.frame_8)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.horizontalLayout_9.addWidget(self.checkBox_14)

        self.lineEdit_12 = QLineEdit(self.frame_8)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_9.addWidget(self.lineEdit_12)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_13 = QCheckBox(self.frame_7)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.horizontalLayout_8.addWidget(self.checkBox_13)

        self.lineEdit_11 = QLineEdit(self.frame_7)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_8.addWidget(self.lineEdit_11)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_10 = QCheckBox(self.frame_6)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.horizontalLayout_7.addWidget(self.checkBox_10)

        self.lineEdit_10 = QLineEdit(self.frame_6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_7.addWidget(self.lineEdit_10)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBox_15 = QCheckBox(self.frame_9)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.horizontalLayout_10.addWidget(self.checkBox_15)

        self.lineEdit_13 = QLineEdit(self.frame_9)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_10.addWidget(self.lineEdit_13)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.checkBox_22 = QCheckBox(self.frame_16)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.horizontalLayout_17.addWidget(self.checkBox_22)

        self.lineEdit_22 = QLineEdit(self.frame_16)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.horizontalLayout_17.addWidget(self.lineEdit_22)


        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.checkBox_20 = QCheckBox(self.frame_14)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.horizontalLayout_15.addWidget(self.checkBox_20)

        self.lineEdit_20 = QLineEdit(self.frame_14)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.horizontalLayout_15.addWidget(self.lineEdit_20)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.checkBox_21 = QCheckBox(self.frame_15)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.horizontalLayout_16.addWidget(self.checkBox_21)

        self.lineEdit_21 = QLineEdit(self.frame_15)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.horizontalLayout_16.addWidget(self.lineEdit_21)


        self.verticalLayout_4.addWidget(self.frame_15)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.checkBox_17 = QCheckBox(self.frame_11)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.horizontalLayout_12.addWidget(self.checkBox_17)

        self.lineEdit_17 = QLineEdit(self.frame_11)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.horizontalLayout_12.addWidget(self.lineEdit_17)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkBox_18 = QCheckBox(self.frame_12)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.horizontalLayout_13.addWidget(self.checkBox_18)

        self.lineEdit_18 = QLineEdit(self.frame_12)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.horizontalLayout_13.addWidget(self.lineEdit_18)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBox_16 = QCheckBox(self.frame_10)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.horizontalLayout_11.addWidget(self.checkBox_16)

        self.lineEdit_14 = QLineEdit(self.frame_10)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_11.addWidget(self.lineEdit_14)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.checkBox_19 = QCheckBox(self.frame_13)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.horizontalLayout_14.addWidget(self.checkBox_19)

        self.lineEdit_19 = QLineEdit(self.frame_13)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.horizontalLayout_14.addWidget(self.lineEdit_19)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.checkBox_23 = QCheckBox(self.frame_17)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.horizontalLayout_18.addWidget(self.checkBox_23)

        self.lineEdit_23 = QLineEdit(self.frame_17)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.horizontalLayout_18.addWidget(self.lineEdit_23)


        self.verticalLayout_4.addWidget(self.frame_17)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(1000, 170, 271, 361))
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 269, 359))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_7, 12, 0, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_27, 7, 0, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_9, 14, 0, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_29, 8, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_10, 11, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color:rgb(70, 0, 5);")

        self.gridLayout.addWidget(self.label_28, 2, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.scrollArea_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 540, 981, 121))
        self.label.setStyleSheet(u"background-color:rgb(0, 30, 25)")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(230, 0, 411, 51))
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
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(1000, 60, 271, 101))
        self.frame_2.setStyleSheet(u"background-color:rgb(20, 81, 109);\n"
"color:rgb(0, 252, 210);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 60, 171, 25))
        self.pushButton.setStyleSheet(u"background-color:rgb(0, 30, 25);\n"
"color:rgb(0, 252, 210);")
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 251, 41))
        self.textEdit.setStyleSheet(u"background-color:rgb(0, 30, 25);\n"
"color:rgb(0, 252, 210);\n"
"font-size:20px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1278, 22))
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"List of Threads", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox.setText("")
        self.checkBox_7.setText("")
        self.checkBox_8.setText("")
        self.checkBox_9.setText("")
        self.checkBox_14.setText("")
        self.checkBox_13.setText("")
        self.checkBox_10.setText("")
        self.checkBox_15.setText("")
        self.checkBox_22.setText("")
        self.checkBox_20.setText("")
        self.checkBox_21.setText("")
        self.checkBox_17.setText("")
        self.checkBox_18.setText("")
        self.checkBox_16.setText("")
        self.checkBox_19.setText("")
        self.checkBox_23.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"PID = 10", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"X = null", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y = <0x56da76cd>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Y = <0x56da76cd>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"name = \"thread\"", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PID = 10", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"List of Expressions", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Teste = 5", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"name = \"thread\"", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"name = \"thread\"", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"X = null", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"X = null", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Teste = 5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"X = null", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"name = \"thread\"", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Inspect Expression", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuControl.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTerminal.setTitle(QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


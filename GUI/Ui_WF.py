# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\NguyenCuong\PrintStamp_A204\GUI\WF.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ApplicationWrapper = QtWidgets.QGroupBox(self.centralwidget)
        self.ApplicationWrapper.setTitle("")
        self.ApplicationWrapper.setObjectName("ApplicationWrapper")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ApplicationWrapper)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SidebarWrapper = QtWidgets.QGroupBox(self.ApplicationWrapper)
        self.SidebarWrapper.setMaximumSize(QtCore.QSize(150, 16777215))
        self.SidebarWrapper.setTitle("")
        self.SidebarWrapper.setObjectName("SidebarWrapper")
        self.Sidebar = QtWidgets.QGroupBox(self.SidebarWrapper)
        self.Sidebar.setGeometry(QtCore.QRect(1, 1, 148, 577))
        self.Sidebar.setStyleSheet("background-color: #fff; border: 1px solid #32a866;")
        self.Sidebar.setTitle("")
        self.Sidebar.setObjectName("Sidebar")
        self.cb_TypeStamp = QtWidgets.QComboBox(self.Sidebar)
        self.cb_TypeStamp.setGeometry(QtCore.QRect(5, 40, 137, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.cb_TypeStamp.setFont(font)
        self.cb_TypeStamp.setStyleSheet("background-color: #fff; border: 2px solid #999; padding: 5px 5px;")
        self.cb_TypeStamp.setObjectName("cb_TypeStamp")
        self.cb_TypeStamp.addItem("")
        self.cb_TypeStamp.addItem("")
        self.LabelSelectStamp = QtWidgets.QLabel(self.Sidebar)
        self.LabelSelectStamp.setGeometry(QtCore.QRect(10, 10, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSelectStamp.setFont(font)
        self.LabelSelectStamp.setStyleSheet("border: none;")
        self.LabelSelectStamp.setObjectName("LabelSelectStamp")
        self.cb_COM = QtWidgets.QComboBox(self.Sidebar)
        self.cb_COM.setGeometry(QtCore.QRect(5, 100, 137, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.cb_COM.setFont(font)
        self.cb_COM.setStyleSheet("background-color: #fff; border: 2px solid #999; padding: 5px 5px;")
        self.cb_COM.setObjectName("cb_COM")
        self.LabelSelectStamp_2 = QtWidgets.QLabel(self.Sidebar)
        self.LabelSelectStamp_2.setGeometry(QtCore.QRect(10, 70, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSelectStamp_2.setFont(font)
        self.LabelSelectStamp_2.setStyleSheet("border: none;")
        self.LabelSelectStamp_2.setObjectName("LabelSelectStamp_2")
        self.LabelSelectStamp_3 = QtWidgets.QLabel(self.Sidebar)
        self.LabelSelectStamp_3.setGeometry(QtCore.QRect(10, 130, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSelectStamp_3.setFont(font)
        self.LabelSelectStamp_3.setStyleSheet("border: none;")
        self.LabelSelectStamp_3.setObjectName("LabelSelectStamp_3")
        self.txt_numberStamp = QtWidgets.QLineEdit(self.Sidebar)
        self.txt_numberStamp.setGeometry(QtCore.QRect(5, 160, 137, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.txt_numberStamp.setFont(font)
        self.txt_numberStamp.setStyleSheet("background-color: #fff; border: 2px solid #999; padding: 5px 5px;")
        self.txt_numberStamp.setObjectName("txt_numberStamp")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Sidebar)
        self.groupBox_3.setGeometry(QtCore.QRect(5, 390, 138, 141))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_58 = QtWidgets.QLabel(self.groupBox_3)
        self.label_58.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.label_58.setStyleSheet("border: none;")
        self.label_58.setObjectName("label_58")
        self.status_form = QtWidgets.QLabel(self.groupBox_3)
        self.status_form.setGeometry(QtCore.QRect(10, 50, 117, 81))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.status_form.setFont(font)
        self.status_form.setStyleSheet("border: none; color: red; font-size: 12px; font-weight: bold;")
        self.status_form.setText("")
        self.status_form.setAlignment(QtCore.Qt.AlignCenter)
        self.status_form.setObjectName("status_form")
        self.btn_Update = QtWidgets.QPushButton(self.Sidebar)
        self.btn_Update.setGeometry(QtCore.QRect(10, 540, 128, 30))
        self.btn_Update.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_Update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Update.setStyleSheet("background-color: #fff; border: 2px solid #999; padding: 5px 5px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\NguyenCuong\\PrintStamp_A204\\GUI\\../PrintStamp_GTK_79/data/icon/update.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Update.setIcon(icon)
        self.btn_Update.setIconSize(QtCore.QSize(20, 20))
        self.btn_Update.setObjectName("btn_Update")
        self.checkBox = QtWidgets.QCheckBox(self.Sidebar)
        self.checkBox.setGeometry(QtCore.QRect(10, 350, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet("border: none;")
        self.checkBox.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.checkBox.setObjectName("checkBox")
        self.btn_Upload = QtWidgets.QToolButton(self.Sidebar)
        self.btn_Upload.setGeometry(QtCore.QRect(5, 230, 137, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_Upload.setFont(font)
        self.btn_Upload.setObjectName("btn_Upload")
        self.LabelSelectStamp_4 = QtWidgets.QLabel(self.Sidebar)
        self.LabelSelectStamp_4.setGeometry(QtCore.QRect(10, 200, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSelectStamp_4.setFont(font)
        self.LabelSelectStamp_4.setStyleSheet("border: none;")
        self.LabelSelectStamp_4.setObjectName("LabelSelectStamp_4")
        self.LabelSelectStamp_5 = QtWidgets.QLabel(self.Sidebar)
        self.LabelSelectStamp_5.setGeometry(QtCore.QRect(10, 270, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LabelSelectStamp_5.setFont(font)
        self.LabelSelectStamp_5.setStyleSheet("border: none;")
        self.LabelSelectStamp_5.setObjectName("LabelSelectStamp_5")
        self.btn_Setting = QtWidgets.QToolButton(self.Sidebar)
        self.btn_Setting.setGeometry(QtCore.QRect(5, 300, 137, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btn_Setting.setFont(font)
        self.btn_Setting.setObjectName("btn_Setting")
        self.horizontalLayout.addWidget(self.SidebarWrapper)
        self.ContentWrapper = QtWidgets.QGroupBox(self.ApplicationWrapper)
        self.ContentWrapper.setTitle("")
        self.ContentWrapper.setObjectName("ContentWrapper")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ContentWrapper)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.ContentWrapper)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.txt_log = PlainTextEdit(self.groupBox)
        self.txt_log.setGeometry(QtCore.QRect(5, 455, 741, 121))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txt_log.setFont(font)
        self.txt_log.setStyleSheet("border: 1px solid #999")
        self.txt_log.setObjectName("txt_log")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 751, 451))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setStyleSheet("border: none; background-color: #fff")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_4)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 451, 451))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Page_1 = QtWidgets.QWidget()
        self.Page_1.setEnabled(False)
        self.Page_1.setObjectName("Page_1")
        self.formLayoutWidget = QtWidgets.QWidget(self.Page_1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 450))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.FormInsert_Box = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.FormInsert_Box.setContentsMargins(2, 2, 2, 2)
        self.FormInsert_Box.setSpacing(2)
        self.FormInsert_Box.setObjectName("FormInsert_Box")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("c")
        self.label.setObjectName("label")
        self.FormInsert_Box.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_Box_SerialNo = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.txt_Box_SerialNo.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_Box_SerialNo.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_Box_SerialNo.setFont(font)
        self.txt_Box_SerialNo.setStyleSheet("border: 1px solid #ccc; font-size: 14px;")
        self.txt_Box_SerialNo.setObjectName("txt_Box_SerialNo")
        self.FormInsert_Box.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_Box_SerialNo)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("c")
        self.label_2.setObjectName("label_2")
        self.FormInsert_Box.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_Box_PN = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.txt_Box_PN.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_Box_PN.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_Box_PN.setFont(font)
        self.txt_Box_PN.setStyleSheet("border: 1px solid #ccc; font-size: 14px;")
        self.txt_Box_PN.setObjectName("txt_Box_PN")
        self.FormInsert_Box.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_Box_PN)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("c")
        self.label_3.setObjectName("label_3")
        self.FormInsert_Box.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_Box_DateCode = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.txt_Box_DateCode.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_Box_DateCode.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_Box_DateCode.setFont(font)
        self.txt_Box_DateCode.setStyleSheet("border: 1px solid #ccc; font-size: 14px;")
        self.txt_Box_DateCode.setObjectName("txt_Box_DateCode")
        self.FormInsert_Box.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_Box_DateCode)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_25.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("c")
        self.label_25.setObjectName("label_25")
        self.FormInsert_Box.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.txt_Box_DataPrint = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.txt_Box_DataPrint.setEnabled(False)
        self.txt_Box_DataPrint.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_Box_DataPrint.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_Box_DataPrint.setFont(font)
        self.txt_Box_DataPrint.setStyleSheet("border: 1px solid #ccc; font-size: 14px; background-color:#eee")
        self.txt_Box_DataPrint.setObjectName("txt_Box_DataPrint")
        self.FormInsert_Box.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_Box_DataPrint)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 60))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_4.setBaseSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.FormInsert_Box.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_4)
        self.stackedWidget.addWidget(self.Page_1)
        self.Page_2 = QtWidgets.QWidget()
        self.Page_2.setObjectName("Page_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.Page_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 441, 441))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.FormInsert_BoxLOT = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.FormInsert_BoxLOT.setContentsMargins(2, 2, 2, 2)
        self.FormInsert_BoxLOT.setSpacing(2)
        self.FormInsert_BoxLOT.setObjectName("FormInsert_BoxLOT")
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_24.setMinimumSize(QtCore.QSize(0, 60))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_24.setBaseSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.FormInsert_BoxLOT.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_24)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_22.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("c")
        self.label_22.setObjectName("label_22")
        self.FormInsert_BoxLOT.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.txt_GlueBoxData = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        self.txt_GlueBoxData.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_GlueBoxData.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_GlueBoxData.setFont(font)
        self.txt_GlueBoxData.setStyleSheet("border: 1px solid #ccc; font-size: 14px;")
        self.txt_GlueBoxData.setObjectName("txt_GlueBoxData")
        self.FormInsert_BoxLOT.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_GlueBoxData)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_28.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("c")
        self.label_28.setObjectName("label_28")
        self.FormInsert_BoxLOT.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.txt_BoxLOT_DataPrint = QtWidgets.QPlainTextEdit(self.formLayoutWidget_2)
        self.txt_BoxLOT_DataPrint.setEnabled(False)
        self.txt_BoxLOT_DataPrint.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_BoxLOT_DataPrint.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.txt_BoxLOT_DataPrint.setFont(font)
        self.txt_BoxLOT_DataPrint.setStyleSheet("border: 1px solid #ccc; font-size: 14px; background-color:#eee")
        self.txt_BoxLOT_DataPrint.setObjectName("txt_BoxLOT_DataPrint")
        self.FormInsert_BoxLOT.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_BoxLOT_DataPrint)
        self.stackedWidget.addWidget(self.Page_2)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_5.setStyleSheet("border: none;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.btn_Reset = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_Reset.setGeometry(QtCore.QRect(10, 290, 271, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Reset.setFont(font)
        self.btn_Reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Reset.setStyleSheet("border: 1px solid #ccc; background-color: #fff;")
        self.btn_Reset.setObjectName("btn_Reset")
        self.btn_Print = PushButton(self.groupBox_5)
        self.btn_Print.setGeometry(QtCore.QRect(10, 250, 131, 31))
        self.btn_Print.setMinimumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Print.setFont(font)
        self.btn_Print.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Print.setStyleSheet("border: 1px solid #ccc; background-color: #fff;")
        self.btn_Print.setObjectName("btn_Print")
        self.btn_CancelPrint = PushButton(self.groupBox_5)
        self.btn_CancelPrint.setGeometry(QtCore.QRect(150, 250, 131, 31))
        self.btn_CancelPrint.setMinimumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_CancelPrint.setFont(font)
        self.btn_CancelPrint.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_CancelPrint.setStyleSheet("border: 1px solid #ccc; background-color: #fff;")
        self.btn_CancelPrint.setObjectName("btn_CancelPrint")
        self.frame_QR = QtWidgets.QLabel(self.groupBox_5)
        self.frame_QR.setGeometry(QtCore.QRect(30, 10, 231, 221))
        self.frame_QR.setStyleSheet("background-color: rgb(222, 222, 222); border: 1px solid #32a866;border-radius: 4px;")
        self.frame_QR.setText("")
        self.frame_QR.setScaledContents(True)
        self.frame_QR.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_QR.setObjectName("frame_QR")
        self.txt_ScanData = QtWidgets.QTextEdit(self.groupBox_5)
        self.txt_ScanData.setGeometry(QtCore.QRect(70, 330, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_ScanData.setFont(font)
        self.txt_ScanData.setStyleSheet("border: 1px solid #ccc; background-color: #fff;")
        self.txt_ScanData.setObjectName("txt_ScanData")
        self.btn_Typing = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_Typing.setGeometry(QtCore.QRect(10, 360, 51, 31))
        self.btn_Typing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Typing.setStyleSheet("font-weight: bold; background-color: #fff; border: 1px solid #ccc")
        self.btn_Typing.setObjectName("btn_Typing")
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.ContentWrapper)
        self.verticalLayout.addWidget(self.ApplicationWrapper)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cb_TypeStamp.setItemText(0, _translate("MainWindow", "GLUE BOX"))
        self.cb_TypeStamp.setItemText(1, _translate("MainWindow", "GLUE LOT"))
        self.LabelSelectStamp.setText(_translate("MainWindow", "Type Stamp:"))
        self.LabelSelectStamp_2.setText(_translate("MainWindow", "COM Printer:"))
        self.LabelSelectStamp_3.setText(_translate("MainWindow", "QTY Stamp:"))
        self.txt_numberStamp.setText(_translate("MainWindow", "1"))
        self.label_58.setText(_translate("MainWindow", "FORM INSERT: "))
        self.btn_Update.setText(_translate("MainWindow", "UPDATE"))
        self.checkBox.setText(_translate("MainWindow", "Keep value"))
        self.btn_Upload.setText(_translate("MainWindow", "xls files..."))
        self.LabelSelectStamp_4.setText(_translate("MainWindow", "Upload Files:"))
        self.LabelSelectStamp_5.setText(_translate("MainWindow", "Settings:"))
        self.btn_Setting.setText(_translate("MainWindow", "SETTING"))
        self.label.setText(_translate("MainWindow", "Box serial No."))
        self.label_2.setText(_translate("MainWindow", "FIT P/N"))
        self.label_3.setText(_translate("MainWindow", "Date Code"))
        self.label_25.setText(_translate("MainWindow", "Data Print"))
        self.label_4.setText(_translate("MainWindow", "GLUE BOX No. Barcode"))
        self.label_24.setText(_translate("MainWindow", "GLUE LOT No. Barcode (GLUE TUPE)"))
        self.label_22.setText(_translate("MainWindow", "Glue Box Data"))
        self.label_28.setText(_translate("MainWindow", "Data Print"))
        self.btn_Reset.setText(_translate("MainWindow", "RESET"))
        self.btn_Print.setText(_translate("MainWindow", "PRINT"))
        self.btn_CancelPrint.setText(_translate("MainWindow", "CANCEL PRINT"))
        self.btn_Typing.setText(_translate("MainWindow", "TYPE"))
from qfluentwidgets import PlainTextEdit, PushButton

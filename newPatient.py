# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newPatient.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 650)
        Dialog.setMinimumSize(QtCore.QSize(400, 650))
        Dialog.setMaximumSize(QtCore.QSize(400, 650))
        Dialog.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"border-radius: 15px;")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 361, 91))
        self.widget.setStyleSheet("QLineEdit {\n"
"    padding-left: 10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.nameLabel = QtWidgets.QLabel(self.widget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 0, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.nameLineEdit.setGeometry(QtCore.QRect(10, 30, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;")
        self.nameLineEdit.setCursorPosition(0)
        self.nameLineEdit.setPlaceholderText("")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(20, 130, 361, 91))
        self.widget_2.setStyleSheet("QLineEdit {\n"
"    padding-left: 10px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.yearsLabel = QtWidgets.QLabel(self.widget_2)
        self.yearsLabel.setGeometry(QtCore.QRect(10, 0, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yearsLabel.setFont(font)
        self.yearsLabel.setObjectName("yearsLabel")
        self.yearsLineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.yearsLineEdit.setGeometry(QtCore.QRect(10, 30, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yearsLineEdit.setFont(font)
        self.yearsLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;")
        self.yearsLineEdit.setCursorPosition(0)
        self.yearsLineEdit.setPlaceholderText("")
        self.yearsLineEdit.setObjectName("yearsLineEdit")
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setGeometry(QtCore.QRect(20, 240, 361, 91))
        self.widget_3.setObjectName("widget_3")
        self.genderLabel = QtWidgets.QLabel(self.widget_3)
        self.genderLabel.setGeometry(QtCore.QRect(10, 0, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.genderLabel.setFont(font)
        self.genderLabel.setObjectName("genderLabel")
        self.radioButtonMale = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonMale.setGeometry(QtCore.QRect(10, 30, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonMale.setFont(font)
        self.radioButtonMale.setObjectName("radioButtonMale")
        self.radioButtonFemale = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonFemale.setGeometry(QtCore.QRect(10, 60, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonFemale.setFont(font)
        self.radioButtonFemale.setObjectName("radioButtonFemale")
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setGeometry(QtCore.QRect(20, 350, 361, 91))
        self.widget_4.setObjectName("widget_4")
        self.addressLabel = QtWidgets.QLabel(self.widget_4)
        self.addressLabel.setGeometry(QtCore.QRect(10, 0, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 201, 31))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    background-color: rgb(255, 255, 255);    /* Pozadina kada nije otvoren */\n"
"    color: #333333;               /* Boja teksta */\n"
"    border-radius: 5px;           /* Zaobljenost ivica */\n"
"    padding: 5px;                 /* Unutrašnji razmak */\n"
"    font-size: 14px;              /* Veličina fonta */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(222, 222, 222);    /* Pozadina kada je miš iznad */\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 2px solid #5c5c5c; /* Ivice između dugmeta za otvaranje */\n"
"    width: 30px;                     /* Širina dugmeta za otvaranje */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons8-drop-down-16.png);   /* Putanja do slike za strelicu nadole */\n"
"    width: 16px;                  /* Širina strelice */\n"
"    height: 16px;                 /* Visina strelice */\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;    /* Pozadina padajuće liste */\n"
"    selection-background-color: rgb(185, 185, 185);  /* Boja pozadine selektovanog elementa */\n"
"    selection-color: rgb(39, 39, 39);     /* Boja teksta selektovanog elementa */\n"
"    font-size: 14px;              /* Veličina fonta za stavke u padajućoj listi */\n"
"    outline: none;\n"
"    \n"
"}")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.widget_5 = QtWidgets.QWidget(Dialog)
        self.widget_5.setGeometry(QtCore.QRect(20, 460, 361, 91))
        self.widget_5.setStyleSheet("QLineEdit {\n"
"    padding-left: 10px;\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.phoneLabel = QtWidgets.QLabel(self.widget_5)
        self.phoneLabel.setGeometry(QtCore.QRect(10, 0, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phoneLabel.setFont(font)
        self.phoneLabel.setObjectName("phoneLabel")
        self.phoneLineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.phoneLineEdit.setGeometry(QtCore.QRect(10, 30, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phoneLineEdit.setFont(font)
        self.phoneLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;")
        self.phoneLineEdit.setCursorPosition(0)
        self.phoneLineEdit.setPlaceholderText("")
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.saveNewPatientButton = QtWidgets.QPushButton(Dialog)
        self.saveNewPatientButton.setGeometry(QtCore.QRect(240, 570, 140, 50))
        self.saveNewPatientButton.setMaximumSize(QtCore.QSize(140, 50))
        self.saveNewPatientButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveNewPatientButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(74, 213, 208);\n"
"    color: rgb(255, 255, 255);\n"
"    width: 115px;\n"
"    height: 45px;\n"
"    font-size:10pt;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(170, 255, 255);\n"
"    color: rgb(132, 132, 132);\n"
"}")
        self.saveNewPatientButton.setObjectName("saveNewPatientButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Patient"))
        self.nameLabel.setText(_translate("Dialog", "Name and Surname"))
        self.yearsLabel.setText(_translate("Dialog", "Year of Birth"))
        self.genderLabel.setText(_translate("Dialog", "Gender"))
        self.radioButtonMale.setText(_translate("Dialog", "Male"))
        self.radioButtonFemale.setText(_translate("Dialog", "Female"))
        self.addressLabel.setText(_translate("Dialog", "Address"))
        self.comboBox.setPlaceholderText(_translate("Dialog", "Odaberi Grad"))
        self.comboBox.setItemText(0, _translate("Dialog", "Tuzla"))
        self.comboBox.setItemText(1, _translate("Dialog", "Srebrenik"))
        self.comboBox.setItemText(2, _translate("Dialog", "Živinice"))
        self.comboBox.setItemText(3, _translate("Dialog", "Gračanica"))
        self.comboBox.setItemText(4, _translate("Dialog", "Gradačac"))
        self.comboBox.setItemText(5, _translate("Dialog", "Kladanj"))
        self.comboBox.setItemText(6, _translate("Dialog", "Sarajevo"))
        self.comboBox.setItemText(7, _translate("Dialog", "Brčko"))
        self.comboBox.setItemText(8, _translate("Dialog", "Olovo"))
        self.comboBox.setItemText(9, _translate("Dialog", "Bijeljina"))
        self.comboBox.setItemText(10, _translate("Dialog", "Zvornik"))
        self.comboBox.setItemText(11, _translate("Dialog", "Drugi Grad"))
        self.phoneLabel.setText(_translate("Dialog", "Phone Number"))
        self.saveNewPatientButton.setText(_translate("Dialog", "Save Patient"))

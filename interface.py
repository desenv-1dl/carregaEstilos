# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def __init__(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 157)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_3 = QtGui.QComboBox(Dialog)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_3)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Carregar Estilos", None))
        self.label.setText(_translate("Dialog", "Selecione a conexão:", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Selecione ...", None))
        self.label_2.setText(_translate("Dialog", "Selecione o tipo de estilos:", None))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Selecione ...", None))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Estilo de Revisão", None))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Estilo de Aquisição", None))
        self.comboBox_3.setItemText(3, _translate("Dialog", "Estilo de Reambulação", None))
        self.comboBox_3.setItemText(4, _translate("Dialog", "Estilo de Vetorização", None))
        self.pushButton.setText(_translate("Dialog", "Carregar", None))


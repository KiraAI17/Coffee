from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 300)
        Form.setWindowTitle("Запись о кофе")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.titleEdit = QtWidgets.QLineEdit(parent=Form)
        self.titleEdit.setPlaceholderText("Название сорта")
        self.verticalLayout.addWidget(self.titleEdit)

        self.roastEdit = QtWidgets.QLineEdit(parent=Form)
        self.roastEdit.setPlaceholderText("Степень обжарки")
        self.verticalLayout.addWidget(self.roastEdit)

        self.typeEdit = QtWidgets.QLineEdit(parent=Form)
        self.typeEdit.setPlaceholderText("Молотый / в зернах")
        self.verticalLayout.addWidget(self.typeEdit)

        self.tasteEdit = QtWidgets.QLineEdit(parent=Form)
        self.tasteEdit.setPlaceholderText("Описание вкуса")
        self.verticalLayout.addWidget(self.tasteEdit)

        self.priceEdit = QtWidgets.QLineEdit(parent=Form)
        self.priceEdit.setPlaceholderText("Цена")
        self.verticalLayout.addWidget(self.priceEdit)

        self.volumeEdit = QtWidgets.QLineEdit(parent=Form)
        self.volumeEdit.setPlaceholderText("Объем упаковки")
        self.verticalLayout.addWidget(self.volumeEdit)

        self.saveBtn = QtWidgets.QPushButton(parent=Form)
        self.saveBtn.setText("Сохранить")
        self.verticalLayout.addWidget(self.saveBtn)

        QtCore.QMetaObject.connectSlotsByName(Form)
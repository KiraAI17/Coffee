from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setWindowTitle("Кофе")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addBtn.setObjectName("addBtn")
        self.addBtn.setText("Добавить")
        self.verticalLayout.addWidget(self.addBtn)
        self.editBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editBtn.setObjectName("editBtn")
        self.editBtn.setText("Изменить выбранное")
        self.verticalLayout.addWidget(self.editBtn)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

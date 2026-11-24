import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from UI.main_ui import Ui_MainWindow
from UI.add_edit_ui import Ui_Form


class AddEditForm(QWidget, Ui_Form):
    def __init__(self, parent, coffee_id=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.coffee_id = coffee_id
        self.edits = [
            self.titleEdit,
            self.roastEdit,
            self.typeEdit,
            self.tasteEdit,
            self.priceEdit,
            self.volumeEdit
        ]

        if coffee_id:
            con = sqlite3.connect("data/coffee.sqlite")
            cur = con.cursor()
            rows = cur.execute("SELECT * FROM coffee WHERE id = ?", (coffee_id,)).fetchall()
            con.close()

            row = rows[0]
            for i in range(len(self.edits)):
                self.edits[i].setText(str(row[i + 1]))

        self.saveBtn.clicked.connect(self.save)

    def save(self):
        vals = []
        for edit in self.edits:
            vals.append(edit.text())

        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()

        if self.coffee_id:
            cur.execute("""UPDATE coffee
                           SET title=?, roast_degree=?, ground_or_beans=?,
                               taste_description=?, price=?, package_volume=?
                           WHERE id=?""", vals + [self.coffee_id])
        else:
            cur.execute("""INSERT INTO coffee
                           (title, roast_degree, ground_or_beans,
                            taste_description, price, package_volume)
                           VALUES (?, ?, ?, ?, ?, ?)""", vals)

        con.commit()
        con.close()
        self.parent.load_table()
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addBtn.clicked.connect(self.add_item)
        self.editBtn.clicked.connect(self.edit_item)
        self.load_table()

    def load_table(self):
        con = sqlite3.connect("data/coffee.sqlite")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM coffee").fetchall()
        con.close()

        headers = ["ID", "Сорт", "Обжарка", "Тип", "Вкус", "Цена", "Объем"]
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.setRowCount(len(data))

        for i in range(len(data)):
            for j in range(len(data[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def add_item(self):
        self.form = AddEditForm(self)
        self.form.show()

    def edit_item(self):
        row = self.tableWidget.currentRow()
        if row != -1:
            coffee_id = self.tableWidget.item(row, 0).text()
            self.form = AddEditForm(self, coffee_id)
            self.form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

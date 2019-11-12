import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem


class DisplayForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.conn = sqlite3.connect('coffee.db')
        self.cursor = self.conn.cursor()
        self.init_ui()

    def init_ui(self):
        self.pb_out.clicked.connect(self.show_info)

    def show_info(self):
        query = 'SELECT * FROM coffee'
        coffee = self.cursor.execute(query).fetchall()
        columns = list(map(lambda x: x[0], self.cursor.description))

        self.tw_info.setRowCount(0)
        self.tw_info.setColumnCount(len(columns))
        self.tw_info.setHorizontalHeaderLabels(columns)

        for row_index, info in enumerate(coffee):
            self.tw_info.insertRow(row_index)

            for col_index, column in enumerate(info):
                self.tw_info.setItem(row_index, col_index, QTableWidgetItem(str(column)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = DisplayForm()
    wnd.show()
    sys.exit(app.exec())

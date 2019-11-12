import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class DisplayForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.init_ui()

    def init_ui(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = DisplayForm()
    wnd.show()
    sys.exit(app.exec())

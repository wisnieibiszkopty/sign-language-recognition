import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from src.widgets.MainWindow import MainWindow


def App():
    app = QtWidgets.QApplication([])
    window = MainWindow()

    #screen = QApplication.primaryScreen()
    #size = screen.availableGeometry()
    #window.resize(size.width(), size.height())

    window.resize(800, 600)

    window.show()
    sys.exit(app.exec())

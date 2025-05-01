from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from src.widgets.CameraWidget import CameraWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Language Recognition")

        layout = QHBoxLayout()
        label = QLabel("Test")

        layout.addWidget(CameraWidget())
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
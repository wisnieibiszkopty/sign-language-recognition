from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from src.SignLanguageModel import SignLanguageModel
from src.widgets.CameraWidget import CameraWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Language Recognition")

        layout = QHBoxLayout()
        label = QLabel("Test")

        model = SignLanguageModel('models/model.keras')

        layout.addWidget(CameraWidget(model))
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from src.SignLanguageModel import SignLanguageModel
from src.widgets.CameraWidget import CameraWidget
from src.widgets.ControlPanelWidget import ControlPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Language Recognition")

        model = SignLanguageModel('models/model.keras')

        self.cameraWidget = CameraWidget(model)
        self.controlPanel = ControlPanel(self.cameraWidget)
        self.cameraWidget.control_panel = self.controlPanel

        layout = QHBoxLayout()
        layout.addWidget(self.cameraWidget)
        layout.addWidget(self.controlPanel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
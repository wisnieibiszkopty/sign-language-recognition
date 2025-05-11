from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QTextEdit


class ControlPanel(QWidget):
    def __init__(self, camera_widget):
        super().__init__()
        self.camera_widget = camera_widget
        self.capture_running = False

        self.last_prediction = None

        self.toggle_button = QPushButton("Start Camera")
        self.toggle_button.clicked.connect(self.toggleCapture)

        self.prediction_text = QTextEdit()
        self.prediction_text.setReadOnly(True)
        self.prediction_text.setPlaceholderText("Recognized signs will appear here...")

        layout = QVBoxLayout()
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.prediction_text)
        self.setLayout(layout)


    def toggleCapture(self):
        if self.capture_running:
            self.camera_widget.stopCapture()
            self.toggle_button.setText("Start Camera")
        else:
            self.camera_widget.startCapture()
            self.toggle_button.setText("Stop Camera")
        self.capture_running = not self.capture_running


    def appendPrediction(self, pred_class):
        if pred_class != self.last_prediction:

            if pred_class == 'space':
                pred_class = " "

            self.prediction_text.insertPlainText(pred_class)
            self.last_prediction = pred_class
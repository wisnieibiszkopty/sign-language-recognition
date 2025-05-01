import cv2
from PIL.ImageQt import QImage, QPixmap
from PySide6 import QtCore

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class CameraWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.cap = cv2.VideoCapture(0)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(30)


    @QtCore.Slot()
    def update(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(img))


    def closeEvent(self, event):
        self.cap.release()
        event.accept()
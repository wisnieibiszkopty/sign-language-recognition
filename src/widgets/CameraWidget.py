from time import sleep

import cv2
import numpy as np
from PIL.ImageQt import QImage, QPixmap
from PySide6 import QtCore

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class CameraWidget(QWidget):
    def __init__(self, model):
        super().__init__()

        self.cap = None
        self.model = model
        self.last_frame = None

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setPointSize(20)

        self.prediction_label = QLabel("Prediction: ")
        self.prediction_label.setAlignment(Qt.AlignCenter)
        self.prediction_label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.prediction_label)
        self.setLayout(layout)

        self.cap_timer = QTimer()
        self.cap_timer.timeout.connect(self.updateFrame)

        self.pred_timer = QTimer()
        self.pred_timer.timeout.connect(self.runPrediction)

        self.setBlackScreen()


    def setBlackScreen(self):
        black_img = np.zeros((480, 640, 3), dtype=np.uint8)
        frame_rgb = cv2.cvtColor(black_img, cv2.COLOR_BGR2RGB)
        h, w, ch = frame_rgb.shape
        img = QImage(frame_rgb.data, w, h, ch * w, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(img))


    def startCapture(self):
        if not self.cap_timer.isActive():
            self.cap_timer.start(20)
        if not self.pred_timer.isActive():
            self.pred_timer.start(200)

        self.cap = cv2.VideoCapture(0)

    def stopCapture(self):
        if self.cap_timer.isActive():
            self.cap_timer.stop()
        if self.pred_timer.isActive():
            self.pred_timer.stop()

        self.setBlackScreen()
        self.cap.release()


    @QtCore.Slot()
    def updateFrame(self):
        ret, frame = self.cap.read()
        if ret:
            self.last_frame = frame
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            img = QImage(frame_rgb.data, w, h, ch * w, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(img))


    @QtCore.Slot()
    def runPrediction(self):
        if self.last_frame is not None:
            frame_rgb = cv2.cvtColor(self.last_frame, cv2.COLOR_BGR2RGB)
            input_img = cv2.resize(frame_rgb, (224, 224))
            input_img = input_img.astype("float32") / 255.0
            input_img = input_img.reshape(1, 224, 224, 3)

            preds = self.model.recognizeSign(input_img)
            pred_class = self.model.labels[np.argmax(preds)]

            print(f"Prediction: {pred_class}")
            self.prediction_label.setText(f"Prediction: {pred_class}")

            if hasattr(self, "control_panel"):
                self.control_panel.appendPrediction(pred_class)


    def closeEvent(self, event):
        self.cap.release()
        event.accept()
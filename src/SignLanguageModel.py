import json
import cv2
import tensorflow as tf
import numpy as np

class SignLanguageModel:
    def __init__(self, model_name):
        try:
            with open('labels.json', 'r') as file:
                labels = json.load(file)
                # reversing dictionary
                self.labels = {v:k for k, v in labels.items()}
                print(self.labels)

            self.model = tf.keras.models.load_model(model_name)
        except FileNotFoundError:
            print("Cannot find file with labels")
        except ValueError:
            print("Cannot find model with this name")


    def recognizeSign(self, image_data):
        return self.model.predict(image_data)


def preprocess(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = frame.astype(np.float32) / 255.0
    return np.expand_dims(frame, axis=0)

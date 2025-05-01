import json
import cv2
import tensorflow as tf
import numpy as np

class SignLanguageModel:
    def __init__(self, model_name):
        try:
            with open('../labels.json', 'r') as file:
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
        return self.model.predict(input_data)


def preprocess(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = frame.astype(np.float32) / 255.0
    return np.expand_dims(frame, axis=0)

image_path = 'nothing.jpg'
image = cv2.imread(image_path)
frame_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
input_data = preprocess(frame_rgb)

# (1, 224, 224, 3)
print(input_data.shape)

model = SignLanguageModel('../models/model.keras')

prediction = model.recognizeSign(input_data)
predicted_class_index = prediction.argmax()
predicted_label = model.labels[predicted_class_index]

print("Prediction: ", prediction)
print("Predicted class: ", predicted_label)

probabilities = prediction[0]

sorted_indices = probabilities.argsort()[::-1]

print("Class\tProbability")
print("-" * 30)
for i in sorted_indices:
    label = model.labels[i]
    prob_percent = probabilities[i] * 100
    print(f"{label:<7}\t{prob_percent:.2f}%")
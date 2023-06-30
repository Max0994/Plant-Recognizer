import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('plant_recognizer_model.h5')

image_width = 224
image_height = 224

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (image_width, image_height))
    image = image / 255.0

    prediction = model.predict(np.expand_dims(image, axis=0))
    predicted_classes = np.argmax(prediction, axis=-1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        if cv2.contourArea(contour) < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        element_image = image[y:y + h, x:x + w]

        if element_image.size == 0:
            continue

        element_image = cv2.resize(element_image, (image_width, image_height))
        element_image = element_image / 255.0
        prediction = model.predict(np.expand_dims(element_image, axis=0))
        predicted_class = np.argmax(prediction)

        if predicted_class == 0:
            label = "plants"
            color = (0, 255, 0)  # Green for "plants"
        elif predicted_class == 1:
            label = "weed"
            color = (0, 0, 255)  # Red for "weed"

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('Video Stream', frame)

    # Break with key 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

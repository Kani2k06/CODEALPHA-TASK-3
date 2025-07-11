import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist


model = load_model("mnist_model.keras")


(_, _), (x_test, y_test) = mnist.load_data()


x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

=
for i in range(5):  
    pred = model.predict(np.expand_dims(x_test[i], axis=0), verbose=0)
    predicted_label = np.argmax(pred)


    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Predicted: {predicted_label}", fontsize=14)
    plt.axis('off')
    plt.show()

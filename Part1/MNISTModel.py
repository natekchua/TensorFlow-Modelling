#For Google Collab
#try:
#  # %tensorflow_version only exists in Colab.
#  %tensorflow_version 2.x
#except Exception:
#  pass

import tensorflow as tf

print("--Get data--")
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("--Process data--")
x_train, x_test = x_train / 255.0, x_test / 255.0

print("--Make model--")
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dropout(0.1),
  tf.keras.layers.Dense(10, activation='sigmoid')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print("--Fit model--")
model.fit(x_train, y_train, epochs=8, verbose=2)

print("--Evaluate Train model--")
model_loss, model_acc = model.evaluate(x_train,  y_train, verbose=2)
print(f"Model Loss:    {model_loss:.2f}")
print(f"Model Accuracy: {model_acc*100:.1f}%")

print("--Evaluate Test model--")
model_loss, model_acc = model.evaluate(x_test,  y_test, verbose=2)
print(f"Model Loss:    {model_loss:.2f}")
print(f"Model Accuracy: {model_acc*100:.1f}%")

#Save Model
model.save('MNIST.h5')
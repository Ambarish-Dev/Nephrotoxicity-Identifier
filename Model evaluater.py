from sklearn.metrics import classification_report, confusion_matrix

# Predict classes with the model
predictions = model.predict(X_test)
predicted_classes = predictions.argmax(axis=-1)
true_classes = y_test.argmax(axis=-1)

# Generate a classification report
print(classification_report(true_classes, predicted_classes, target_names=class_names))

# Generate a confusion matrix
conf_matrix = confusion_matrix(true_classes, predicted_classes)
print(conf_matrix)

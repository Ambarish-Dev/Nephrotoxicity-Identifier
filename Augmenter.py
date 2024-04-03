from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define an image data generator for augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# Assuming X_train contains your images and they're in the correct shape for your CNN
augmented_images = datagen.flow(X_train, y_train, batch_size=32)  # y_train are your labels

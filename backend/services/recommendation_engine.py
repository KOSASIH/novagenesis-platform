import pandas as pd
import numpy as np
import tensorflow as tf

class RecommendationEngine:
    def __init__(self, user_item_matrix):
        self.user_item_matrix = user_item_matrix
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Embedding(input_dim=100, output_dim=50),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def train(self):
        self.model.fit(self.user_item_matrix, epochs=10)

    def predict(self, user_id):
        user_vector = self.user_item_matrix[user_id]
        predictions = self.model.predict(user_vector)
        return predictions

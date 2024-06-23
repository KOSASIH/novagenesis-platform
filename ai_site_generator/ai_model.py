import tensorflow

class AiModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = tensorflow.keras.models.load_model(self.model_path)

    def generate_site(self, input_data):
        # Generate site using AI model
        output_data = self.model.predict(input_data)
        return output_data

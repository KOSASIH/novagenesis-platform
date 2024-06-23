class SiteGenerator:
    def __init__(self, ai_model):
        self.ai_model = ai_model

    def generate_site(self, input_data):
        # Generate site using AI model
        output_data = self.ai_model.generate_site(input_data)
        return output_data

class ApiRoutes:
    def __init__(self, web_app):
        self.web_app = web_app

    def create_routes(self):
        # Create API routes
        @self.web_app.app.route('/api/generate-site', methods=['POST'])
        def generate_site_api():
            input_data = flask.request.get_json()
            output_data = self.web_app.site_generator.generate_site(input_data)
            return flask.jsonify({'site': output_data})

        return self.web_app.app

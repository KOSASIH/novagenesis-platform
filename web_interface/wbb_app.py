import flask

class WebApp:
    def __init__(self, site_generator):
        self.site_generator = site_generator
        self.app = flask.Flask(__name__)

    def create_app(self):
        # Create Flask app
        @self.app.route('/')
        def index():
            return 'Welcome to Novagenesis Platform!'

        @self.app.route('/generate-site', methods=['POST'])
        def generate_site():
            input_data = flask.request.get_json()
            output_data = self.site_generator.generate_site(input_data)
            return flask.jsonify({'site': output_data})

        return self.app

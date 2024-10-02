from flask import Flask

def create_app():
    app = Flask(__name__)

    # Basic route for testing
    @app.route('/')
    def index():
        return "Hello World!"
    
    return app
from src.config import Config
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.controllers import HealthController


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    app.app_context().push()
    api = Api(app)
    api.add_resource(HealthController, "/health")
    return app


app = create_app()
app.config["MAX_CONTENT_LENGTH"] = 1024


def run():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    run()

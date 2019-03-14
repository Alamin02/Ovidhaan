from flask import Flask
from flask_cors import CORS
from dictionary import api_blueprint
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(api_blueprint, url_prefix='/api')

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.root_path, 'database', 'database.db'),
    )

    CORS(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from resources import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    _app = create_app()
    _app.debug = True
    _app.run()

import json
from os import environ

from blueprints import home_blueprint
from celery import Celery, Task
from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


redis_client = FlaskRedis()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def init_api(app):
    from resources import BookListResource, BookResource

    api = Api(app)
    # Register resources with API
    api.add_resource(BookResource, "/books/<int:book_id>")
    api.add_resource(BookListResource, "/books")


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app


def create_app() -> Flask:
    environment = environ.get("ENVIRONMENT", "local")
    app = Flask(__name__)
    app.config.from_file(f"{environment}.json", load=json.load)

    app.register_blueprint(home_blueprint)

    celery_init_app(app)
    redis_client.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    init_api(app)
    return app


app = create_app()

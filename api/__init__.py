from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_graphql import GraphQLView
from .schema import schema
from .database import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .blueprints.main import main_bp
    app.register_blueprint(main_bp)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # Enable GraphiQL interface
        )
    )
    
    return app
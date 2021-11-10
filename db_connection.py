from flask_sqlalchemy import SQLAlchemy

def get_db_connection(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db = SQLAlchemy(app)
    return app
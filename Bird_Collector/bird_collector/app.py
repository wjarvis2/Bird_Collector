"""Main application and routing logic for Bird_Collector."""
from flask import Flask, render_template
from .models import DB, User


def create_app():
    """Create and configure an instance of the Flask Application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)
    
    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!') 

    return app
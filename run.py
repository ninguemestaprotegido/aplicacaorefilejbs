from app import create_app, db
from flask_migrate import Migrate
import os

app = create_app()




migrate = Migrate(app, db) 

if __name__ == "__main__":
    app.run(debug=True)

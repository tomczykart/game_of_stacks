from app import app
from app import db
from app.models import User, UserCube

import os


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'UserCube': UserCube}


if __name__ == "__main__":  # Makes sure this is the main process
	app.run(debug=True, port=8080, host='0.0.0.0')
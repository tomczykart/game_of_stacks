from app import app
from app import db
import os
from app.models import User, UserCube


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'UserCube': UserCube}


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host=os.environ.get('IP', '0.0.0.0'),  # EStablishes the host, required for repl to detect the site
		port=int(os.environ.get('PORT', 8080)),  # Randomly select the port the machine hosts on.
    debug=True
	)
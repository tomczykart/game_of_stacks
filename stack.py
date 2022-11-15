from app import app
from app import db
from app.models import User, UserCube


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'UserCube': UserCube}


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)
from functools import wraps
from flask import redirect, flash, url_for
from flask.login import current_user

def check_confirmed(fc):
    @wraps(fc)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            flash('Please confirm your account')
            return redirect(url_for('unconfirmed'))
        return fc(*args, **kwargs)
    return decorated_function
    
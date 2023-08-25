from flask import Blueprint, render_template


# register blueprint
home_bp = Blueprint("home", __name__, template_folder="templates")


# Home view
@home_bp.route("/index", methods=("GET", "POST"))
def index():
    return render_template("index.html")

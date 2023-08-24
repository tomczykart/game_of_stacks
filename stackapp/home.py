from flask import Blueprint


# register blueprint
bp = Blueprint("home", __name__, template_folder="templates")


# home view
@bp.route("/home", methods=("GET", "POST"))
def home():
    return "This is home page"
    # return render_template("home/home.html")

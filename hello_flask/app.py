import flask
import flask_login

app = flask.Flask(__name__)
app.secret_key = "super secret string"  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
class User(flask_login.UserMixin):
    def __init__(self, email, password):
        self.id = email
        self.password = password

users = {"leafstorm": User("leafstorm", "secret")}@app.get("/login")
def login():
    return """<form method=post>
      Email: <input name="email"><br>
      Password: <input name="password" type=password><br>
      <button>Log In</button>
    </form>"""

@app.post("/login")
def login():
    user = users.get(flask.request.form["email"])

    if user is None or user.password != flask.request.form["password"]:
        return flask.redirect(flask.url_for("login"))

    flask_login.login_user(user)
    return flask.redirect(flask.url_for("protected"))

@app.route("/protected")
@flask_login.login_required
def protected():
    return flask.render_template_string(
        "Logged in as: {{ user.id }}",
        user=flask_login.current_user
    )

@app.route("/logout")
def logout():
    flask_login.logout_user()
    return "Logged out"
from flask import Flask, jsonify, render_template, request  # pyright: ignore[reportMissingImports]
from .routes.interview_routes import interview_bp
#from ai_mock_interview.app import app
app = Flask(__name__)
app.register_blueprint(interview_bp)

@app.errorhandler(500)
def handle_server_error(error):
    if request.path in {"/start", "/next", "/monitor", "/end"}:
        return jsonify({"error": "Server could not process the interview request."}), 500
    return error

@app.route("/")
def home():
    return render_template("interview.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
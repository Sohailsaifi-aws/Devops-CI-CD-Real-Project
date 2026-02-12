from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Pipeline</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                padding-top: 100px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>🚀 CI/CD Pipeline is Working!</h1>
        <p>Your Flask application is successfully deployed.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask
from grupo_01.routes import grupo_bp

app = Flask(__name__)
app.register_blueprint(grupo_bp)

if __name__ == "__main__":
    app.run(debug=True)

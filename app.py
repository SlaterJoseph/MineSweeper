from flask import Flask
from Web.Game.controller import gameplay_bp

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

app.register_blueprint(gameplay_bp)


@app.route('/')
def index():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)
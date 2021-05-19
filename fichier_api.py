import flask
from flask import Flask
from flask import jsonify
from fonction import ouvrire_fichier
app = Flask(__name__)

@app.route('/')
def hello_world():
    """def hello_world : Display hello world
    """
    return jsonify('Hello, World!')


@app.route('/ouvrire_fichier/')
def ouvrire_fichier():
    return jsonify(ouvrire_fichier())








if __name__ == "__main__":
    app.run(debug=True)
"""
App WSGI que serve o site estático do TCC (site_tcc/index.html).

No PythonAnywhere, aponte o arquivo de configuração WSGI para:
    from flask_app import app as application

Localmente:
    python flask_app.py
    # e acesse http://localhost:5000
"""
import os

from flask import Flask, send_from_directory, abort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(BASE_DIR, "site_tcc")

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(SITE_DIR, "index.html")


@app.route("/<path:path>")
def site_files(path):
    full = os.path.join(SITE_DIR, path)
    if os.path.isfile(full):
        return send_from_directory(SITE_DIR, path)
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)

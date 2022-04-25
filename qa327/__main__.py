from qa327 import app, frontend

"""
This file runs the server at a given port
"""

FLASK_PORT = 8081

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=FLASK_PORT)

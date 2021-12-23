from flask import Flask
from testserver import endpoints
from testserver import database


app = Flask(__name__)


endpoints.init_app(app)
database.init_app(app)


# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)

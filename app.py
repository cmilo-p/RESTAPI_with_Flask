from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBluprint
from resources.store import blp as StoreBluprint

app = Flask(__name__)

app.cpnfig["PROPAGATE_EXCEPTIONS"] = True
app.cpnfig["API_TITLE"] = "Stores REST API"
app.cpnfig["API_VERSION"] = "V1"
app.cpnfig["OPENAPI_VERSION"] = "3.0.3"
app.cpnfig["OPENAPI_URL_PREFIX"] = "/"
app.cpnfig["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.cpnfig["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBluprint)
api.register_blueprint(StoreBluprint)
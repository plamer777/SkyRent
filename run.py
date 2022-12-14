"""This is a main file to start the application"""
import os
import dotenv
from flask_cors import CORS
from configs import DevelopConfig
from views.real_estate import real_estate_ns
from views.locations import location_ns
from utils import create_app, add_namespaces, api
# -------------------------------------------------------------------------
dotenv.load_dotenv()
os.environ['FLASK_MODE'] = 'development'
# ------------------------------------------------------------------------
config = DevelopConfig()
app = create_app(config)
add_namespaces(api, [real_estate_ns, location_ns])
CORS(app)


if __name__ == '__main__':

    app.run(ssl_context='adhoc')

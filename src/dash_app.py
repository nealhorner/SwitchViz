import os
from dash import Dash
from flask_caching import Cache

dash_app = Dash()

cache = Cache(
    dash_app.server,
    config={
        "CACHE_TYPE": "filesystem",
        "CACHE_DIR": os.path.join(os.getcwd(), "cache"),
    },
)

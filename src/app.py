import os
from dash import Dash
from flask_caching import Cache

app = Dash()

cache = Cache(
    app.server,
    config={
        "CACHE_TYPE": "filesystem",
        "CACHE_DIR": os.path.join(os.getcwd(), "cache"),
    },
)

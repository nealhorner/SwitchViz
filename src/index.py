from dash_app import dash_app
from layout import app_layout
import callbacks  # noqa: F401

dash_app.layout = app_layout
app = dash_app.server

if __name__ == "__main__":
    app.run(debug=True)

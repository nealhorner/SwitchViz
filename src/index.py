from app import app
from layout import app_layout
import callbacks  # noqa: F401

app.layout = app_layout

if __name__ == "__main__":
    app.run(debug=True)

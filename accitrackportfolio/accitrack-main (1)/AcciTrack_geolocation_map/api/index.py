import os, sys

# Make the project root importable (main.py, db_tables.py live one level up)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app as _flask_app  # noqa: E402


class _FixPath:
    """Safety net: if the platform hands Flask the function path instead of
    the real URL, treat it as the home page rather than a 404."""

    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        if environ.get("PATH_INFO") in ("/api/index", "/api/index.py"):
            environ["PATH_INFO"] = "/"
        return self.wsgi_app(environ, start_response)


app = _FixPath(_flask_app)  # Vercel looks for the "app" object

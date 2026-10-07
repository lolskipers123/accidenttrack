import os, sys

# Make the project root importable (main.py, db_tables.py live one level up)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app  # noqa: E402,F401  (Vercel looks for the "app" object)

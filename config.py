import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Database connection string
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'].replace('postgres','postgresql')
# Supress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
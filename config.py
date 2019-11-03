import os

class Config():
    # grabs current base directory name
    basedir = os.path.abspath(os.path.dirname(__file__))
    # places sqlite database in this directory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False





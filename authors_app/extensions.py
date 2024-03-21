from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_bcrypt import Bcrypt
#from flask_bcrypt import Bcrypt

db = SQLAlchemy()

migrate = Migrate()

bcypt = Bcrypt()

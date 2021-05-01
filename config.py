import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsdb-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms-database'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsdbadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Cmsdbpass1'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'teststoreaccud'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'I9xQCvE/KZFAKAlKRJfUXe3ZfkbIhormDHqbWTb8pjU/KhS6nUTwO3WcNbCmuzFBj7F4YCW6jX2WLBrkSLZiLQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'image'

import os
class Config:
    
    # MOVIE_API_BASE_URL ="https://api.themoviedb.org/3/movie/{}?api_key={}"
    # MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = '450922fba6e46eeb36b12d8a7635aa92836d3dbe'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/bloggy'

    DEBUG = True

config_options ={
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig}


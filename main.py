from app import app
from app.lib.db import Factory

if __name__ == '__main__':
    Factory(
        app=app,
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://newuser:password@localhost/petition'
    ).make()

    app.run()

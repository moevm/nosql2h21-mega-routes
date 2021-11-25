from flask_script import Manager
from neomodel import config

from web_app.app import create_app
from web_app.db import connect

config.DATABASE_URL = 'bolt://neo4j:testpass@localhost:11003'

app = create_app()
app.app_context().push()

manager = Manager(app)

if __name__ == "__main__":
    manager.run()

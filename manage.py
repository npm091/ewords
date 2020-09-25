from flask_script import Manager, Server
from ewords import app
from ewords.scripts.db import InitDB, InsertTable


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.add_command('insert_table', InsertTable())
    manager.add_command("runserver", Server(
        host=app.config['HOST'], port=app.config['PORT'], use_debugger=True, use_reloader=True))
    manager.run()

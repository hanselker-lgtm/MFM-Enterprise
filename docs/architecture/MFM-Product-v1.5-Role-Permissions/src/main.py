from src.database.db import Database
from src.database.schema import initialize_schema
from src.application.context import ApplicationContext
from src.gui.main_window import MainWindow

def start_app():
    db = Database()
    initialize_schema(db)
    context = ApplicationContext(db)
    app = MainWindow(context)
    app.run()

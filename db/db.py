from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from backend.db.db_models import Base
from flask import g
from flask import Flask
import os

class DbConnection:
    def __init__(self, connection_string: str, echo: bool = False):
        
        self.engine = create_engine(connection_string, echo = echo)
        Base.metadata.create_all(self.engine)

    def Insert(self, model: any):
        with Session(self.engine) as session:
            session.add(model)
            session.commit()

def initDB(app: Flask):
    
    with app.app_context():
        db_conn: str = "sqlite:///" + app.config["DATABASE"]
        filename: str = app.config["DATABASE"]
        if 'db' not in g:
            g.db = DbConnection(db_conn)

def getDB() -> DbConnection:
    db_conn: str = "sqlite://" + app.config["DATABASE"]
    if 'db' not in g:
        g.db = DbConnection(db_conn)
    return g.db
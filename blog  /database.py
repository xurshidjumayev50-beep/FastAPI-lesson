from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_bas
from sqlalchemy.orm import sessionmaker
SQLALCHAMY_DATAASE_URL = 'sqlite:///./blog.db'

engina=create_engine(SQLALCHAMY_DATAASE_URL,connect_arggs={"check_same_threread":False})
SessionLocal =sessionmaker(bind=engina,autocommit=False,autoflush=False)

Base=declarative_bas()
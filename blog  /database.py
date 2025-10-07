from sqlalchemy import create_engine

engina=create_engine('sqlite:///./blog.db:memory:',echo=True)
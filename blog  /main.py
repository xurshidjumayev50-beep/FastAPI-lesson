from fastapi import FastAPI



from . import schemas


from . import schemas, models


from .database import engine

app = FastAPI()




models.Base.metadata.create_all(engine)





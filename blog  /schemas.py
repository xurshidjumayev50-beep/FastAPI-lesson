

from pydantic import BaseModel


class Blog(BaseModel):

body: str




    class Config():


        orm_mode = True


        orm_mode = True





class User(BaseModel):


    name:str


    email:str


    password:str
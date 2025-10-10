

from typing import List


from pydantic import BaseModel






class Blog(BaseModel):


    title: str


    body: str





class ShowBlog(BaseModel):


class BlogBase(BaseModel):

    title: str

    body: str




class Blog(BlogBase):

    class Config():

        orm_mode = True



@@ -20,5 +18,14 @@ class User(BaseModel):

class ShowUser(BaseModel):

    name:str

    email:str


    blogs : List[Blog] =[]


    class Config():


        orm_mode = True





class ShowBlog(BaseModel):


    title: str


    body:str


    creator: ShowUser




    class Config():

        orm_mode = True
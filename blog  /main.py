from sqlalchemy import Column, Integer, String



from sqlalchemy import Column, Integer, String, ForeignKey

from .database import Base


from sqlalchemy.orm import relationship





class Blog(Base):

@@ -8,6 +9,10 @@ class Blog(Base):

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    body = Column(String)


    user_id = Column(Integer, ForeignKey('users.id'))





    creator = relationship("User", back_populates="blogs")






class User(Base):

    __tablename__ = 'users'

@@ -16,3 +21,5 @@ class User(Base):

    name = Column(String)

    email = Column(String)

    password = Column(String)





    blogs = relationship('Blog', back_populates="creator")


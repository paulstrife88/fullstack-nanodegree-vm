import sys

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context


Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	email = Column(String(50), nullable = False)
	password_hash = Column(String(64))

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)

class Item(Base):
	__tablename__ = 'item'

	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	description = Column(String(250), nullable = False)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
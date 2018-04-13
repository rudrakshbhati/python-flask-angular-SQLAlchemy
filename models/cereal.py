from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey,Float
from sqlalchemy.orm import relationship
from base import Base



class Cereal(Base):
	__tablename__ = 'cereals'


	name = Column(String, primary_key=True)

	def __init__(self,name):
		self.name = name
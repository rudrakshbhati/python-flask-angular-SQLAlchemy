from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey,Float
from sqlalchemy.orm import relationship
from base import Base



class Mandi(Base):
	__tablename__ = 'mandi'

	name = Column(String , primary_key=True)
	state = Column(String, primary_key=True)
	
	def __init__(self,name,state):
		self.name = name
		self.state = state
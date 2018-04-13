from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey,Float,ForeignKeyConstraint
from sqlalchemy.orm import relationship
from base import Base
from mandi import Mandi


class DailyData(Base):
	__tablename__ = 'ddata'

	market = Column(String, primary_key=True)
	state = Column(String, primary_key = True)
	arrivals = Column(Float)
	unit_of_arrivals = Column(String)
	origin = Column(String)
	variety = Column(String)
	minimum_price = Column(Float)
	maximum_price = Column(Float)
	modal_price = Column(Float)
	unit_of_price = Column(String)
	cereal = Column(String, ForeignKey('cereals.name'), primary_key = True)
	reported_on = Column(Date, primary_key = True)
	__table_args__ = (ForeignKeyConstraint([market,state],[Mandi.name,Mandi.state]), {})

	def __init__(self,
		market,
		arrivals ,
		unit_of_arrivals, 
		origin , 
		variety,
		minimum_price ,
		maximum_price,
		modal_price,
		unit_of_price,
		cereal,
		reported_on,
		state
		):

		self.market = market
		self.arrivals = arrivals
		self.unit_of_arrivals = unit_of_arrivals
		self.origin = origin
		self.variety = variety
		self.minimum_price  = minimum_price
		self.maximum_price = maximum_price
		self.modal_price = modal_price
		self.unit_of_price = unit_of_price



		self.cereal = cereal
		self.reported_on = reported_on
		self.state = state

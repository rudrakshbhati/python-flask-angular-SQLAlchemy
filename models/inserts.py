from datetime import date
from mandi import Mandi
from base import Session, engine, Base
from cereal import Cereal
from daily_data import DailyData
from data_parser import parser_data
from sqlalchemy import exc





Base.metadata.create_all(engine)

session = Session()

def insert(for_cereal = False, for_mandi = False, for_ddata = False):
	cereals, mandis, ddata = parser_data()
	if for_cereal:
		cereals.pop(0)
		for cereal in cereals:
			data_object = Cereal(cereal)
			session.add(data_object)
			try_except()
	
	if for_mandi:
		for mandi in mandis:
			data_object =  Mandi(mandi[0],mandi[1])
			session.add(data_object)
			try_except()
	
	if for_ddata:
		for data in ddata:
			for x in [1,5,6,7]:
				if str(data[x]) == 'NR' :
					data[x] = None
			data_object =  DailyData(*data)
			session.add(data_object)
			try_except()

def try_except():
	try:
		session.commit()
	except exc.SQLAlchemyError as e:
		session.rollback()
		print "error",e.message
	finally:
		session.close()


# insert(for_cereal = True,for_mandi=True,for_ddata = True)


from base import Session
from datetime import date
from daily_data import DailyData
from cereal import Cereal
from mandi import Mandi

extract a session
session = Session()


def get_names(cereal = False,mandi = False):
	if cereal or mandi:
		if cereal:
			_data = session.query(Cereal).all()
		if mandi:
			_data = session.query(Mandi).all()
		names = []
		for data in _data:
			names.append(data.name)
		return names
	else:
		return None

def get_mandis():
	_data = session.query(Cereal).all()
	cereals = []
	for data in _data:
		cereals.append(data.name)
	return cereals


def get_price(crop_name,mandi,d):
	if not isinstance(d, (list,tuple)):
		price_data = []
		# date is of format mm/dd/yyyy
		_date = date(int(d.split('/')[2]),int(d.split('/')[1]),int(d.split('/')[0]) )
		_data = session.query(DailyData).filter(DailyData.cereal == crop_name)\
		.filter(DailyData.market == mandi)\
		.filter(DailyData.reported_on == _date )\
		.all() 
		for data in _data:
			price_data.append({
				'cereal':data.cereal,
			 	'mandi' : data.market,
			 	'state' : data.state,
			 	'modal_price':data.modal_price })
		return price_data
	if isinstance(d, (list,tuple)):
		price_data = {}
		d1 , d2  = d[0], d[1]
		# date is of format mm/dd/yyyy
		_date1 = date( int(d1.split('/')[2]),int(d1.split('/')[1]),int(d1.split('/')[0]) )
		_date2 = date( int(d2.split('/')[2]),int(d2.split('/')[1]),int(d2.split('/')[0]) )
		_data = session.query(DailyData).filter(DailyData.cereal == crop_name)\
		.filter(DailyData.market == mandi)\
		.filter(DailyData.reported_on >_date1 )\
		.filter(DailyData.reported_on <_date2 )\
		.all()
		for data in _data:
			if str(data.reported_on) in price_data:
				price_data[str(data.reported_on)].append({
				'cereal':data.cereal,
			 	'mandi' : data.market,
			 	'state' : data.state,
			 	'modal_price':data.modal_price
			 	})
			else:
				price_data[str(data.reported_on)] = [{
				'cereal':data.cereal,
			 	'mandi' : data.market,
			 	'state' : data.state,
			 	'modal_price':data.modal_price
			 	}]

		return price_data















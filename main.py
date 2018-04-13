from flask import Flask, render_template,jsonify,json, request
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
from models import queries as q
from datetime import datetime


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
	return render_template('view.html'),200
# to get cereal name and mandi
@app.route('/get_names/<entity>')
def get_name(entity):
	if entity == "cereal":
		cereals = q.get_names(cereal = True)
		return jsonify(cereals=cereals), 200

	if entity == "mandi":
		mandis  = q.get_names(mandi = True)
		return jsonify(mandis = mandis), 200


# to get price(if single date given) or price range(if both) for given mandi and cereal
@app.route('/get_price',methods = ['GET','POST'])
def get_price():
	_data = request.get_json() or json.loads(request.data) if request.data else {}
	if  not _data.get("cereal") and not _data.get("mandi"):
		return "Please provide cereal AND mandi", 400

	if  not _data.get("date1") and not _data.get("date2"):
		return "Please provide a date", 400

	if _data.get("date1") and _data.get("date2"):
		d1 = datetime.strptime(_data.get("date1"), '%m/%d/%Y').date()
		d2 = datetime.strptime(_data.get("date2"), '%m/%d/%Y').date()

		if d1 > d2:
			return "Please select date in proper order",400

		dates = [_data.get("date1"),_data.get("date2")]
		price_data = q.get_price(_data.get("cereal"),_data.get("mandi"),dates)

	else:
		if _data.get("date1"):
			price_data = q.get_price(_data.get("cereal"),_data.get("mandi"),_data.get('date1'))
		else:
			price_data = q.get_price(_data.get("cereal"),_data.get("mandi"),_data.get('date2'))
	return jsonify(price_data = price_data)





if __name__ == "__main__":
	app.run()
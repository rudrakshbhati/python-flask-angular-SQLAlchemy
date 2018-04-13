from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

FILES = [
	"Agriculture Marketing_mar_1",
	"Agriculture Marketing_mar_2",
	"Agriculture Marketing_mar_3",
	"Agriculture Marketing_mar_6",
	"Agriculture Marketing_mar_7"
]


def data_parser(file_name):
	with open('../templates/data4parse/'+ file_name + '.html') as the_file:
		soup = BeautifulSoup(the_file,"lxml")
	dt = soup.find(id = "cphBody_lblTitle").getText()
	date = dt.split(":")[1]
	soup_2 = soup.find(id = "cphBody_GridView1")
	table = soup_2.find("table")
	rows = soup_2.find_all("tr")
	table_contents,header_cells = [],[]
	state = ""
	cereal = ""
	_data = {}
	cereals = []
	markets_states = []
	ddata = []

	for tr in rows:

		if rows.index(tr) == 0 : 
			header_cells = [ th.getText().strip() for th in tr.find_all('th') if th.getText().strip() != '' ]  
		if rows.index(tr) == 1 :
			pass
		else :
			row_cells = ([ tr.find('th').getText() ] if tr.find('th') else [] ) + [ td.getText().strip() for td in tr.find_all('td') if td.getText().strip() != '' ]

		table_contents += [ row_cells ]

	for i in range(len(table_contents)):
		if len(table_contents[i]) < 2:
			temp = table_contents[i+1]
			if len(temp) < 2:
				cereal = table_contents[i][0]
				if cereal not in cereals:
					cereals.append(cereal)
				state = temp[0]

			else:
				state = table_contents[i][0]

		else:
			if cereal in _data:
				if state in _data[cereal]:
					_data[cereal][state].append(table_contents[i])	
				else:
					_data[cereal].update({state: [table_contents[i]]})
			else:
				_data.update({cereal:{state:[table_contents[i]]}})
			if len(table_contents[i]) > 8:
				if (table_contents[i], state) not in markets_states:
					markets_states.append((table_contents[i][0], state))

				table_contents[i].extend([cereal,date,state])
				ddata.append(table_contents[i])
	return cereals,markets_states,ddata


def parser_data():
	n = len(FILES)
	c = []
	m = []
	d = []
	for file in FILES:
		cereals,markets_states,ddata = data_parser(file)
		c.extend(cereals)
		m.extend(markets_states)
		d.extend(ddata)

	return c, m, d

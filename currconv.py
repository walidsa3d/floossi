import json,requests,csv
from sys import argv

script,amount,src,dest=argv
def getFullName(curr):
	currencies = csv.reader(open("ISOCurrencyCodes.csv"))
	for row in currencies:
		if row[0].lower()==curr.lower():
			return row[1]

def convertcurrency():
	r  = requests.get("http://rate-exchange.appspot.com/currency?from="+src+"&to="+dest)
	data = json.loads(r.text)
	exchange=float(amount)*data['rate']
	result=amount+" "+getFullName(src)+" = "+str(exchange)+" "+getFullName(dest)
	return result

print convertcurrency()


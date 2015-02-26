import json
import requests
import csv
from sys import argv
import pyparsing as p

class Currconv:
	def __init__(self):
		self.codes="currencycodes.csv"

	def getFullName(self,curr):
		currencies = csv.reader(open(self.codes))
		for row in currencies:
			if row[0].lower()==curr.lower():
				return row[1]

	def convertcurrency(self,amount,src,dest):
		url="http://rate-exchange.appspot.com/currency?from={0}&to={1}".format(src,dest)
		r  = requests.get(url)
		data = json.loads(r.text)
		exchange=float(amount)*data['rate']
		print "Rate=",data['rate']
		result=amount+" "+self.getFullName(src)+" = "+str(exchange)+" "+self.getFullName(dest)
		return result
	def parse_args(self,ar):
		amount=p.Word(p.nums)
		src=p.Word(p.alphas)
		dest=p.Word(p.alphas)
		inn=p.Optional("in").suppress()
		query=(amount+src+inn+dest)
		tokens = query.parseString(ar) 
		return tokens
	def main(self):
		args=self.parse_args(" ".join(argv[1:]))
		print self.convertcurrency(args[0],args[1],args[2])

if __name__ == '__main__':
	Currconv().main()




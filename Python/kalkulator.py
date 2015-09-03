# Kalkulator - Polish-notation calculator

from itertools import groupby
from operator import *

class Kalkulator:
	def __init__(self):
		self.operators = ('+', '-', '/', '*', '^')
		self.operacje = (add, sub, div, mul, pow)
		self.opers = dict(zip(self.operators, self.operacje))
		self.wejscie = []
		self.petla()
	
	def get_wejscie(self):
		wejscie = raw_input()
		while not wejscie:
			wejscie = raw_input()
		self.wejscie = wejscie.split(" ") if " " in wejscie else list(wejscie)
		
		
	def render_wejscie(self, wejscie):
		groups = []
		last = None
		
		def grouper(x):
			if x in self.operators:
				return x
				
		for key, group in groupby(wejscie, grouper):
			if key:
				last = key
			else:
				groups.append((last, tuple(group)))
		return tuple(groups)
				
	def dzialac(self, wejscie):
		wejscie = self.render_wejscie(wejscie)
		
		def kalkulate(pozycja):
			for op, inni in [pozycja]:
				action = self.opers[op]
				rest = tuple(map(int, inni))
				if (len(rest) < 2):
					return rest
				return int(action(*rest))
		
		results = map(kalkulate, wejscie)
		total = 0
		for i in results:
			if (type(i) == tuple):
				i = i[0]
			total+=i
		return total
		
		
	def petla(self):
		while True:
			try:
				self.get_wejscie()
				print self.dzialac(self.wejscie)
			except KeyboardInterrupt, EOFError:
				break
			except TypeError:
				print 'NaN'
				continue
		
		
kalk = Kalkulator()

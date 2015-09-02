# Kalkulator - Polish-notation calculator

class Kalkulator:
	def __init__(self):
		self.operators = ('+', '-', '/', '*', '^')
		self.operations = ('add', 'sub', 'div', 'mul', 'pow')
		self.opers = tuple(zip(self.operators, self.operations))
		self.wejscie = []
		self.get_wejscie()
	
	def get_wejscie(self):
		wejscie = raw_input()
		while not wejscie:
			wejscie = raw_input()
		self.wejscie = wejscie.split(" ") if " " in wejscie else list(wejscie)
		
		
kalk = Kalkulator()
print kalk.wejscie
print kalk.opers

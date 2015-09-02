
class Kalkulator:
	def __init__(self):
		self.operands = ['+', '-', '/', '*', '^']
		self.wejscie = []
		self.get_input()
	
	def get_input(self):
		wejscie = raw_input()
		while not wejscie:
			wejscie = raw_input()
		self.wejscie = wejscie.split(" ") if " " in wejscie else list(wejscie)
		
		
kalk = Kalkulator()
print kalk.wejscie

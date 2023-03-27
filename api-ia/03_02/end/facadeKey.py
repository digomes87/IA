class SubsystemA:

	def method1(self):
		print('SubsystemA method1 ...')
		
	def method2(self):
		print('SubsystemA method2 ...')

class SubsystemB:
	
	def method1B(self):
		print('SubsystemB method1 B ...')
		
	def method2B(self):
		print('SubsystemB method2 B ...')

class Facade:

	def __init__(self):
		self._subsystem_A = SubsystemA()
		self._subsystem_B = SubsystemB()

	def method(self):
		self._subsystem_A.method1()
		self._subsystem_A.method2()
		
		self._subsystem_B.method1B()
		self._subsystem_B.method2B()

def main():
	facade = Facade()
	facade.method()

if __name__ == "__main__":
	main()

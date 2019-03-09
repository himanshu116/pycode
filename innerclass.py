class inner1:
	def __init__(self):
		print("outer class constructor")
		class inner:
			def __init__(self):
				print("inner class constructor")

				a1=inner1()
				a2=a1.inner()
				del a1
				print(id(a2))
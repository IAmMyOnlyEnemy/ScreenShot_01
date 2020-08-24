

class Person:
	"This is a person class"

	def __init__(self, a=10, s='boy'):
		self.age = a
		self.sex = s

	def greet(self):
		print("Hello! I am a {0} of {1} years old.".format(self.sex,self.age))

harry = Person(15, 'girl')

print(Person.greet)
print(harry.greet)

harry.greet()

class Polygon:
	def __init__(self, nr_of_sides):
		self.n = nr_of_sides
		self.sides = [0 for i in range(nr_of_sides)]
	def inputSides(self):
		self.sides = [float(
							input("Enter side" + str(i+1)+" : ")
							)for i in range(self.n)]
	def dispSides(self):
		for i in range(self.n):
			print("Side {0} is {1}".format(i+1,self.sides[i]))

class Triangle(Polygon):
	def __init__(self):
		Polygon.__init__(self,3)
	def findArea(self):
		a, b, c = self.sides
		s = (a + b + c) / 2
		area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print('The area of the triangle is {0}'.format(area))

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
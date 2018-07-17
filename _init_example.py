class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def myfunct(self):
        print("hello my name is" + self.name)


p2 = person("amulya", 213)
p2.myfunct()
print(p2.name)

del p2.age
print(p2.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



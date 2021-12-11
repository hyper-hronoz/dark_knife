from abc import ABC,abstractclassmethod

class Parent(ABC):

    @abstractclassmethod
    def pqr(self):
        pass


class Child(Parent):
	pass

obj = Child()
obj.pqr()
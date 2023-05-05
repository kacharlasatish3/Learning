# Multiple inheritance
class father:
    def get_mylands(self):
        print("father properties")

    def get_my_business(self):
        print("Father business")


class mother:
    def get_myhouses(self):
        print("mother house properties")

    def get_my_business(self):
        print("Mother business")


class spouse:
    def get_my_business(self):
        print("Spouce business")


class child(mother, father, spouse):
    def get_myhouses(self):
        super().get_myhouses()
        print("changed mother house")

    def get_mylands(self):
        super().get_mylands()
        print("changed father properties")

    def get_my_business(self):
        # super will call immediate parent method
        super().get_my_business()
        # to call explicitly use class name by passing self
        # mother.get_my_business(self)
        # father.get_my_business(self)
        # spouse.get_my_business(self)
        print("child businesss")


# MRO  => method resolution order
obj_child = child()
obj_child.get_myhouses()
obj_child.get_mylands()
obj_child.get_my_business()

# class ,object,abstraction,encapsulation,polymorphism,inheritance
# self,constructor,class methods,instance methods,static methods,super

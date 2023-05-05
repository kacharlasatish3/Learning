# Inheritance => Its parent and child relation , where child can access the functionality from parent and
# child can override/extend the functionality

class parent:
    def get_my_house(self):
        print("2 floor building from parent")

    def get_plots(self):
        print("Father earned 2 plots")

class child(parent):
    def get_lands(self):
        print("My earned lands")

    def get_my_house(self):
        super().get_my_house()
        print("4 floor from child")


# override => defining parent method/functon in child class to override/extend the functionality of parent
# super => this is used to access parent methods/functions from child class


print("////////child classs//////")
obj_child = child()
obj_child.get_my_house()
obj_child.get_lands()

print("///////Parent class//////")
obj_parent = parent()
obj_parent.get_my_house()


# Single level
# Multilevel
# Multiple

# Single level => inheritance from one parent and child , single level
# Multi level => inheritance will be extended to multilevel children
class grandchild(child):
    def get_plots(self):
        print("Overriden grand parents plots")


print("///////grand child////")
obj_grandchild = grandchild()
obj_grandchild.get_my_house()
obj_grandchild.get_lands()
obj_grandchild.get_plots()



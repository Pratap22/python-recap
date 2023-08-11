#     Father  (1 acre plot land)
#       |
#      Son    (1 acre plot land)


# define a superclass
# class Father:
#     # attributes and method definition
    
#     total_land = "300 Acres"

#     def display(self):
#         print(f"The total land area is: ", self.total_land)

# # inheritance
# class Son(Father):
#     # attributes and method of super_class
#     # attributes and method of sub_clas
#     no_of_girlfirends = 2

#     def print_gf_count(self):
#         print(f"The number of GF's are: ", self.no_of_girlfirends)

# son = Son()
# dad = Father()

# # print(son.total_land)
# # print(dad.total_land)

# son.display()
# son.print_gf_count()

# dad.display()
# dad.print_gf_count()

#Base calss
class Polygon:
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputsides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.no_of_sides)]

    def display_sides(self):
        for i in range(self.no_of_sides):
            print(f"Side {i+1} is {self.sides[i]}")

# SUbclass
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def find_area(self):
        a,b,c = self.sides
        # semi-perimeter
        s = (a+b+c)/2

        # By using Heron's formula
        area =(s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle is %0.2f"%area)

    def display_sides(self):
        super().display_sides()
        print("The sides are ", self.sides)

t = Triangle()
t.inputsides()
t.display_sides()
t.find_area()
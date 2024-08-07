class Shape:
    name = "circle"

    def change_name(self,new_name):
        self.name=new_name


s = Shape()
s.change_name("Triangle")
print(s.name)



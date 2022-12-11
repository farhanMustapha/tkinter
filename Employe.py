class Employee:
    def __init__(self,name,age,departement,is_manager):
        self.name=name
        self.age=age
        self.departement=departement
        self.is_manager=is_manager


employee1=Employee("islam",50,"codezilla",True)
employee2=Employee("hasan",30,"facebook",False)

print(employee2.age)

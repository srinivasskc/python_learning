# Created by Srinivas Kadiyala at 20-02-2023

class Person:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots movie")

    def speaks(self):
        if self.occupation == "tennis player":
            print(self.name, "speaks russian language")
        elif self.occupation == "actor":
            print(self.name, "speaks american english language")


tom = Person("Tom Cruise", "actor")
maria = Person("Maria", "tennis player")
tom.do_work()
tom.speaks()
maria.do_work()
maria.speaks()


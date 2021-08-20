# Duck Typing
# If there is an object i.e 'ide' and it has method 'execute' then we, are not concern about which class object is,
# we concern about it should have that method 'execute'--called Duck Typing


class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("Spell Checking")
        print("Convention Checking")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor() # Object ide

lap1 = Laptop() # Object lap1
lap1.code(ide)
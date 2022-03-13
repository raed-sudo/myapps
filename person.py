class Person():
    #attribute
    race='Human'
    nationality='Tunisian'

    def __init__(self, name) -> None:
        # Constructor
        self.name = name

    def say_hello(self) -> str:
        # method
        return('Hello ' + self.name)
    
    def get_name(self) -> str:
        return self.name


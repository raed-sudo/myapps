class Calculator():
    def __init__(self) -> None:
        pass

    def add(self,x,y) -> float:
        return x + y
        
    def substract(self,x,y) -> float:
        return x - y

    def multiply(self,x,y) -> float:
        return x * y

    def add(self,x,y) -> float:
        if x == 0 : 
            raise ValueError('Can not divide by zero !')
        return x / y
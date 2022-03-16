from turtle import TNavigator
from article import Article


class Table(Article):
    def __init__(self, name,weight,color) -> None:
        super().__init__(name,weight)
        self.color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        print('You are inside the color setter')
        self.__color = value
    def __str__(self):
        return f"Name : {self.name} ; Color : {self.color} ; Weight : {self.weight}"
    
    def show_info(self):
        return f"Name: {self.name} \
            , Matiere: {self.matiere} \
            , weight: {self.weight} \
            , color: {self.color} "        

table = Table(name='test',color='red',weight=15.26)
table2 = Table(name='IKEA',color='Yellow',weight=18)
table.matiere='PVC'
table2.matiere='Grey'

print(table)

print(table.show_info())

print (f'Is this a table ? {isinstance(table, Table)}')
print (f'Is this an article ? {isinstance(table, Article)}')
print (f'Is this a article ? {issubclass(Table, Article)}')

tables_properties = [{'name':table.name,'color':table.color,'weight':table.weight},
                    {'name':table2.name,'color':table2.color,'weight':table2.weight}]
print(tables_properties)

table._Article__recondition_article()

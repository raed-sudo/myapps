from configparser import MAX_INTERPOLATION_DEPTH


class Article():
    def __init__(self,name,weight)-> None:
        self.name=name
        self.weight=weight


    @property
    def name(self):
        return self.__name 
    @name.setter
    def name(self,value):
        #cool validation here
        if value != '':
            self.__name = value
        else:
            print('Name cannot be NULL')
    
    @property
    def matiere(self):
        return self.__matiere
    @matiere.setter
    def matiere(self,value:str):
        print('In the setter of matiere')
        self.__matiere = value
        
    @property
    def weight(self):
        return self.__weight 
    @weight.setter
    def weight(self,value:float):
        print('In the setter of weight')
        self.__weight = value  

    def show_info(self) :
        return f"Article Name : {self.name} \
            , Matiere : {self.matiere} \
            , weight: {self.weight}"

    def __recondition_article(self):
        del(self)
        print ('Article reconditioned')

from configparser import MAX_INTERPOLATION_DEPTH


class Article():
    matiere=''
    def __init__(self,name)-> None:
        self.name=name

    def get_matiere(self) -> str:
        return self.matiere

    def set_matiere(self,matiere) -> None:
        self.matiere=matiere

    def set_weight(self,weight:float) -> None:
        self.weight=weight

    def get_weight(self) -> float:
        return self.weight

    def display_article(self) :
        return f"Article Name : {self.name} \
            , Matiere fabricatiob : {self.matiere} \
            , article weight: {self.weight}"
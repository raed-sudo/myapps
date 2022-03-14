from article import *

article = Article('test')

article.matiere = 'plastique'
article.weight = 1.526

print(article.get_matiere())

print(article.display_article())
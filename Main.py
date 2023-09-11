from Class import Manga
from Class import Rangement_livre
import pandas


lecture = pandas.read_excel("Lecture.xlsx", usecols='A:D')

index = 0 
Liste_manga = []
print(lecture)
while (index<len(lecture)):
    lecture.Nom[index] = lecture.Nom[index].lower()
    lecture.Nom[index] = Manga(lecture.Nom[index],lecture.chapter_saison[index],lecture.Statut_episode[index] )
    Liste_manga.append(lecture.Nom[index])
    index+=1

print(Liste_manga)

Excel = Rangement_livre(Liste_manga)
element = Excel.Trie()

data_to_export = [{"Nom" : element.name, "chapter_saison" : element.chapter ,"Statut_episode" : element.episode}for element in Excel.list]
data_frame_to_export =  pandas.DataFrame.from_records(data_to_export)
data_frame_to_export.to_excel("Lecture.xlsx", sheet_name='result')

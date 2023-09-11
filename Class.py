class Manga:
  def __init__(self, name, chapter,episode):
    self.name = name
    self.chapter = chapter
    self.episode = episode



class Rangement_livre:
  def __init__(self, List_Livre):
    self.list_name=[]
    self.list = []
    for k in range(len(List_Livre)):
      self.list_name.append(List_Livre[k].name)
      self.list.append(List_Livre[k])
     
  def Trie(self):
    self.list_name = sorted( self.list_name)  
    list_temporaire = []
    for i in self.list_name:
      j=0
      while(i!=self.list[j].name):
        j+=1
      list_temporaire.append(self.list[j])
    self.list = list_temporaire
    return list_temporaire
  
  def ajouter(self, livre):
    self.list.append(livre)
  
          
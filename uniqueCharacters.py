class CharacterManipulation:
  def __init__(self, string_chaine):
      self.string_chaine = string_chaine.lower()
      self.unique_char = True
      print ("Original string: ", self.string_chaine)
      self.check_characters
      
  def check_characters(self):
      characters = [char for char in self.string_chaine]
      characters_list = []
      for character in characters:
            if character in characters_list:
                self.unique_char = False
                break
            else:
                characters_list.append(character)
                characters_list.sort()
                
input_string = CharacterManipulation("Cracking")                

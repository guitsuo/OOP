# Overriding e super 

# Então, herança é boa para adicionar novos comportamentos para classes existentes, 
# mas e sobre comportamentos que mudam? 

# Nossa classe "contact" permite apenas um nome e um endereço de e-mail
# E se quisessemos adicionar um numero de telefone para nossos amigos? 

# Poderiamos sobrescrever o __init__ 
# Sobrescrever é alterar ou repor um método da superclasse com um novo método (com o mesmo nome na subclasse 

class ContactList(list):
  def search(self, name):

    matching_contacts = []

    for contact in self:
      if name in contact.name:
        matching_contacts.append(contact)
    return matching_contacts
    
class Contact:

  all_contacts = ContactList()

  def __init__(self, name, email):
    self.name = name
    self.email = email
    Contact.all_contacts.append(self) 
class Friend(Contact):
  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone 

# Qualquer método pode ser sobrescrito, não apenas __init__ 
# O problema é que o código é duplicado... 

# O que realmente precisamos é uma maneira de executar o método __init__ inicial na classe Contact
# Isso é o que a função super faz.. retorna o objeto como uma instância da classe pai:

class Friend(Contact):
  def __init__(self, name, email, phone):
    super().__init__(name, email)
    self.phone = phone 

# Esse método primeiro pega a instância do objeto pai usando super e chama __init__ naquele objeto. 
# passando os argumentos esperados
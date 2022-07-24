# teste

class Contact:
    all_contacts = []

    def __init__(self, name=None, email=None, **kwargs):
        #super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street=None, city=None, state=None, code=None, **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

s = Friend(name = 'a', email  = 'b')
print(s.name)
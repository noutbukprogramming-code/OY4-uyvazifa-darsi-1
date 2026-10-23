class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def update_phone(self, new_phone):
        self.phone = new_phone

    def show_info(self):
        print(f"Ism: {self.name}\nTelefon: {self.phone}")


contact = Contact('Malika', '901234567')
contact.update_phone('931112233')
contact.show_info()
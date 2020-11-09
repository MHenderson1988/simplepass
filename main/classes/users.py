class Users:
    def __init__(self, aName):
        self.name = str(aName)
        self.password_list = {}

    def change_name(self, aName):
        self.name = aName

    def add_password(self, aWebsite, aPassword):
        self.password_list[aWebsite] = aPassword

class Users:
    def __init__(self, aName):
        self.name = str(aName)
        self.password_list = {}

    """
    Takes one input, a string which will be the user's new name.
    """

    def change_name(self, aName):
        self.name = aName

    """
    This method allows the user to add a new website/password key value pair.  Once added, the dictionary is sorted
    into alphabetical order.
    
    The method takes two inputs, both strings, a website and a password
    """

    def add_password(self, aWebsite, aPassword):
        self.password_list[aWebsite] = aPassword
        self.password_list = {k: self.password_list[k] for k in sorted(self.password_list)}

    """
    Takes a single input, a string representing a website, and deletes the corresponding key in the dictionary.
    """

    def remove_website(self, aWebsite):
        del self.password_list[aWebsite]

    """
    Takes two inputs of the type String.  The name of the website to replace and the new website with which is shall be
    replaced.  Once completed the dictionary is sorted into alphabetical order.
    """

    def edit_website_name(self, oldName, newName):
        self.password_list[newName] = self.password_list.pop(oldName)
        self.password_list = {k: self.password_list[k] for k in sorted(self.password_list)}

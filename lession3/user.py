class User:

    def __init__(self, first_name, last_name):
        self.userfname = first_name
        self.userlname = last_name

    def fName(self):
        print("мое имя ", self.userfname)

    def lName(self):
        print("моя фамилия ", self.userlname)

    def flName(self):
        print("меня зовут ", self.userfname, self.userlname)

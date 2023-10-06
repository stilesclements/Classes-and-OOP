#Write a class named Patient that has the following attributes - ID, name, address, phone, veteran_status (True or False). 
#The Patient class’s __init__ method should accept an argument for each attribute. The Patient class should have accessor 
#methods only for each attribute.

class Patient:
    def __init__(self,Ident,n,add,ph,vet):
        self.ID=Ident
        self.name=n
        self.address=add
        self.phone=ph
        self.veteran_status=vet
    def get_ID(self):
        return self.ID
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_phone(self):
        return self.phone
    def get_veteran_status(self):
        return self.veteran_status
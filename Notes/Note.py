import datetime

class Note:
    def __init__(self,ident,name,body):
        self.ident = ident
        self.name = name
        self.body = body
        self.data = datetime.date.today()
        self.time = datetime.datetime.now().time()

    def edit_body(self,nbody):
        self.body = nbody
        self.data = datetime.date.today()
        self.time = datetime.datetime.now().time()

    def edit_name(self,nname):
        self.name = nname
        self.data = datetime.date.today()
        self.time = datetime.datetime.now().time()
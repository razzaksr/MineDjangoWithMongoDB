from mongoengine import *
class Candidate(Document):
    studentid = IntField(required=True)
    name = StringField(max_length=50)
    age = IntField()
    def _init__(self, id, name, age):
        self.studentid=id,
        self.name=name
        self.age=age
    def __str__(self):
        return str(self.studentid)+" "+self.name+" "+str(self.age)+"\n"    
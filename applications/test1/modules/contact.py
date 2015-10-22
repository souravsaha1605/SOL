from gluon import current
from gluon.dal import DAL, Field
from gluon.sqlhtml import SQLFORM
from gluon.validators import IS_NOT_EMPTY, IS_EMAIL, IS_LENGTH
 
 
class Contact(object):
    """Build a Contact object"""
 
    def __init__(self):
        self.db = DAL("sqlite://mydb.sqlite")
        self.session = current.session
        self.request = current.request
        self.response = current.response
        self.cache = current.cache
        self.define_table()
        self.set_validators()
 
    def define_table(self):
        self.contact = self.db.define_table("contact",
                Field("name"),
                Field("email"),
                Field("phone")
         )
 
    def set_validators(self):
        self.contact.name.requires = IS_NOT_EMPTY()
        self.contact.email.requires = IS_EMAIL()
        self.contact.phone.requires = IS_LENGTH(14)
 
    def form(self, formstyle):
        return SQLFORM(self.contact, formstyle=formstyle).process()
 
    def load(self, scope, limitby=None):
        queries = {"all": self.contact.id>0,
                   "gmailers": self.contact.email.like("%gmail.com%")}
        return self.db(queries[scope]).select(limitby=limitby)

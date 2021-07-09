# from django.db import models

from neomodel import (StructuredNode, StringProperty,
                      IntegerProperty,UniqueIdProperty,
                      RelationshipTo,BooleanProperty,
                      DateTimeProperty)


# Create your models here.
class User(StructuredNode):
    __abstract_node__ = True
    uid = UniqueIdProperty()
    SEXES = {'F': 'Female', 'M': 'Male', 'O': 'Other'}
    first_name = StringProperty(unique_index=True)
    last_name = StringProperty(unique_index=True)
    sex = StringProperty(required=True, choices=SEXES)
    is_admin= BooleanProperty(unique_index=False,default=None)
    is_user = BooleanProperty(unique_index=False,default=None)
    password = StringProperty()
    created = DateTimeProperty(default_now=True)


class UserMixin(object):
    name = StringProperty(unique_index=True)
    password = StringProperty()


class City(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
    name = StringProperty(index=True, default="city")


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # Relations :
    city = RelationshipTo(City, 'LIVES_IN')
    friends = RelationshipTo('Person','FRIEND')


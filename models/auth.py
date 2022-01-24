from flask_mongoengine import MongoEngine, Document
from mongoengine import StringField, BooleanField, DateTimeField, ListField, ReferenceField
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, auth_required, hash_password

# Create database connection object
# db = MongoEngine(app)

class Role(Document, RoleMixin):
    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)
    permissions = StringField(max_length=255)

class User(Document, UserMixin):
    email = StringField(max_length=255, unique=True)
    password = StringField(max_length=255)
    active = BooleanField(default=True)
    fs_uniquifier = StringField(max_length=64, unique=True)
    confirmed_at = DateTimeField()
    roles = ListField(ReferenceField(Role), default=[])
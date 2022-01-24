from flask_mongoengine import Document
from mongoengine import StringField, ListField, ReferenceField
from models import User    

# Create database connection object
# db = MongoEngine(app)

class InstagramImage(Document):
    image_url = StringField(max_length=255)
    user = ReferenceField(User)

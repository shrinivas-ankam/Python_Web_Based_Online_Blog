import uuid
import datetime
from common.database import Database

class Post(object):
    def __init__(self,blog_id,title,content,author,create_date=datetime.datetime.utcnow(),_id=None):
        self.blog_id=blog_id
        self.title=title
        self.content=content
        self.author=author
        self._id=uuid.uuid4().hex if _id is None else _id
        self.create_date=create_date

    def save_to_mongo(self):
        Database.insert(collection='posts',data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'create_date':self.create_date,
            }

    @classmethod
    def from_mongo(cls,id):
        post_data = Database.find_one(collection="posts",query={"_id":id});
        return cls(**post_data)


    @staticmethod
    def from_posts(id):
        return [post for post in Database.find(collection="posts", query={"blog_id": id})];
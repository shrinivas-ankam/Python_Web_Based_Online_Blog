import uuid
import datetime
from models.post import Post
from common.database import Database

class Blog(object):
    def __init__(self,author,title, description,author_id,_id=None):
        self.author = author
        self.title = title
        self.description = description
        self.author_id=author_id
        self._id = uuid.uuid4().hex if id is None else _id

    def new_post(self,title,content,date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    create_date=datetime.datetime.strptime(date,"%d%M%Y"))
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_posts(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author':self.author,
            'author_id':self.author_id,
            'title':self.title,
            'description':self.description,
            '_id':self._id
        }

    @classmethod
    def from_mongo(cls,id):
        blog_data=Database.find_one(collection='blogs',query={'_id':id})
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls,author_id):
        blogs=Database.find_one(collection='blogs',query={'author_id':author_id})
        return [cls(**blog) for blog in blogs]

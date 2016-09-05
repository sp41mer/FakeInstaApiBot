__author__ = 'sp41mer'
import peewee
database = peewee.PostgresqlDatabase(
    'instagram',
    user='root',
    password='root',
    host='localhost'

)
class Profile(peewee.Model):
    date = peewee.CharField(default='', null=True)
    count = peewee.IntegerField(default=0, null=True)
    followers = peewee.TextField(default='', null=True)

    class Meta:
        database = database

class Friendship(peewee.Model):
    date = peewee.CharField(default='', null=True)
    followed = peewee.TextField(default='', null=True)
    followed_counter = peewee.IntegerField(default=0, null='True')
    unfollowed = peewee.TextField(default='', null=True)
    unfollowed_counter = peewee.IntegerField(default=0, null='True')
    class Meta:
        database = database

class Users(peewee.Model):
    pk = peewee.BigIntegerField(index=True)
    full_name = peewee.CharField(default='', null=True)
    has_anonymous_profile_picture = peewee.CharField(default='', null=True)
    is_private = peewee.CharField(default='', null=True)
    is_verified = peewee.CharField(default='', null=True)
    profile_pic_url = peewee.CharField(default='', null=True)
    username = peewee.CharField(default='', null=True)
    insta_link = peewee.CharField(default='', null=True)
    class Meta:
        database = database

def create_tables():
    database.connect()
    try:
        database.create_tables([Profile,Friendship,Users], True)
    except Exception as e:
        print(str(e))

#create_tables()
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

def create_tables():
    database.connect()
    try:
        database.create_tables([Group], True)
    except Exception as e:
        print(str(e))

create_tables()
__author__ = 'sp41mer'
import datetime
from InstagramAPI import InstagramAPI
from models import MyLikes, Users

InstagramAPI = InstagramAPI("testing_accaunt", "cgfhnfrxtvgbjy1922")
InstagramAPI.login()
InstagramAPI.getSelfUserFeed()
self_feed = InstagramAPI.LastJson
likers = []
for item in self_feed['items'][:5]:
    InstagramAPI.getMediaLikers(item['id'])
    for user in InstagramAPI.LastJson['users']:
        likers.append(user['pk'])
users_for_like = set(likers)
date = datetime.datetime.now()
for liker in users_for_like:
    try:
        Users.get(Users.pk == liker)
        print("All right, it's just follower")
    except Users.DoesNotExist:
        if (InstagramAPI.getUserFeed(liker)):
            try:
                MyLikes.get(MyLikes.user_pk == liker)
                print("I've already liked it")
            except MyLikes.DoesNotExist:
                media_id = InstagramAPI.LastJson['items'][0]['id']
                InstagramAPI.like(media_id)
                MyLikes.create(
                    date=date,
                    user_pk=liker,
                    media_id=media_id
                )
__author__ = 'sp41mer'
import datetime
from InstagramAPI import InstagramAPI
from models import Users,Profile, Friendship

InstagramAPI = InstagramAPI("testing_accaunt", "cgfhnfrxtvgbjy1922")
InstagramAPI.login()
InstagramAPI.searchUsername('princegeorgii')
media_id = InstagramAPI.LastJson
followers = InstagramAPI.getTotalFollowers(media_id['user']['pk'])
followers_ids = []
for follower in followers:
    followers_ids.append(follower['pk'])
    try:
        Users.get(
            Users.pk == follower['pk']
        )
    except Users.DoesNotExist:
        Users.create(
                pk=follower['pk'],
                full_name=str(follower['full_name']),
                has_anonymous_profile_picture = str(follower['has_anonymous_profile_picture']),
                is_private = str(follower['is_private']),
                is_verified = str(follower['is_verified']),
                profile_pic_url = str(follower['profile_pic_url']),
                username = str(follower['username']),
                insta_link = 'https://www.instagram.com/'+str(follower['username'])+'/'
        )
date = datetime.datetime.now()


for item in Profile.select().order_by(Profile.id.desc()).limit(1):
    previous_followers = list(map(int,item.followers.split()))
unfollow = set(previous_followers) - set(followers_ids)
follow = set(followers_ids) - set(previous_followers)
unfollow_len = len(unfollow)
follow_len = len(follow)
follow_str = " ".join(str(pk) for pk in follow)
unfollow_str = " ".join(str(pk) for pk in follow)
Friendship.create(
    date = date,
    followed = follow_str,
    followed_counter = follow_len,
    unfollowed = unfollow_str,
    unfollowed_counter = unfollow_len,
)
followers_string = " ".join(str(pk) for pk in followers_ids)
Profile.create(
    date=date,
    count=len(followers_ids),
    followers=followers_string
)




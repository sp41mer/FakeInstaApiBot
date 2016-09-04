__author__ = 'sp41mer'
from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("testing_accaunt", "cgfhnfrxtvgbjy1922")
InstagramAPI.login()
InstagramAPI.searchUsername('anastasiias_23')
media_id = InstagramAPI.LastJson
followers = InstagramAPI.getTotalFollowers(media_id['user']['pk'])
print(followers)
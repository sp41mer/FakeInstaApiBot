__author__ = 'sp41mer'
from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("testing_accaunt", "cgfhnfrxtvgbjy1922")
InstagramAPI.login()
InstagramAPI.searchUsername('princegeorgii')
media_id = InstagramAPI.LastJson
followers = InstagramAPI.getTotalFollowers(media_id['user']['pk'])
print(followers)

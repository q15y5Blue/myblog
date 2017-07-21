from django.db import models
# 使用ORM框架

# class Article(models.Model):
#     title = models.CharField(max_length=32, default='Title')
#     content = models.TextField(null=True)

# http://travel.qunar.com/space/158928832@qunar
# http://travel.qunar.com/space/follow/list?userId=158928832&page=1
class Persons(models.Model):
    identify = models.CharField(max_length=32,default='user_identify_id')
    name = models.CharField(max_length=32,default='user_name')
    describe = models.CharField(max_length=1000,default='user_describe')
    followings = models.TextField()
    fans = models.TextField()
    # 151310985,158928832,5931438

    def getFollowingsToList(self):
        return self.followings.split(',')
    def setListToFollowings(self,list):
        self.describe = ','.join(list)
    def getFans(self):
        return self.fans.split(',')
    def setListToFans(self,list):
        self.fans= ','.join(list)


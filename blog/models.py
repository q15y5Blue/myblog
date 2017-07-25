from django.db import models
# 使用ORM框架

# class Article(models.Model):
#     title = models.CharField(max_length=32, default='Title')
#     content = models.TextField(null=True)


# http://travel.qunar.com/space/158928832@qunar
# http://travel.qunar.com/space/follow/list?userId=158928832&page=1
class Persons(models.Model):
    identify = models.CharField(max_length=32, default='user_identify_id')
    name = models.CharField(max_length=32, default='user_name')
    describe = models.CharField(max_length=1000, default='user_describe')
    followings = models.TextField()
    fans = models.TextField()
    followings_number = models.IntegerField(max_length=16,default='user_followings_numbers')# 关注人数
    fans_number = models.IntegerField(max_length=16,default='user_fans_numbers')             # 粉丝人数
    # 151310985,158928832,5931438

    def get_following_str_to_list(self):
        return self.followings.split(',')

    def set_following_list_to_str(self, list):
        self.followings = ','.join(list)

    def get_fans_str_to_list(self):
        return self.fans.split(',')

    def set_fans_list_to_str(self,list):
        self.fans=','.join(list)

    # 获取关注的人数
    def set_followings_number(self):
        return len(self.get_following_str_to_list())

    # 获取粉丝人数
    def set_fans_number(self):
        return len(self.get_fans_str_to_list())

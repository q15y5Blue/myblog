from django.db import models
# 使用ORM


# 用户
class Persons(models.Model):
    identify = models.IntegerField(default='user_identify_id', unique=True)
    name = models.CharField(max_length=32, default='user_name')
    describe = models.CharField(max_length=1000, default='user_describe')
    followings = models.TextField()
    fans = models.TextField()
    followings_number = models.IntegerField(default='user_followings_numbers')# 关注人数
    fans_number = models.IntegerField(default='user_fans_numbers')             # 粉丝人数
    # 151310985, 158928832, 5931438

    @property
    def get_following_str_to_list(self):
        return self.followings.split(',')

    def set_following_list_to_str(self, list):
        self.followings = ','.join(list)

    @property
    def get_fans_str_to_list(self):
        return self.fans.split(',')

    def set_fans_list_to_str(self, list):
        self.fans = ','.join(list)

    # 获取关注的人数
    def set_followings_number(self):
        return len(self.get_following_str_to_list)

    # 获取粉丝人数
    def set_fans_number(self):
        return len(self.get_fans_str_to_list)


# 游记   一游记多标题  一标题多内容
class Travels(models.Model):
    travel_create_data = models.DateField(default='travel_create_data')   # 创建日期
    travel_view_number = models.IntegerField(default='travel_view_number')
    travel_commended = models.BooleanField(default='travel_commend')
    travel_when = models.DateField(default='travel_date')
    travel_how_long = models.IntegerField(default='travel_spend_time')
    travel_how_much = models.IntegerField(default='travel_cost')
    travel_who = models.CharField(max_length=30, default='travel_who')
    travel_how = models.CharField(max_length=30, default='travel_how')
    travel_user = models.ForeignKey(Persons, on_delete=models.CASCADE)  # 多对一 多个游记对一个人


# 游记下的标题分类
class TravelsCatalog(models.Model):
    catalog_title = models.CharField(max_length=32, default='travel_catalog_title')


# 游记下的标题分类下的内容
class TravelsCatalogContent(models.Model):
    content_type = models.CharField(max_length=64, default='travel_cat_type')
    content_title = models.CharField(max_length=128, default='travel_cat_content')  # 文本标题 或 景点标题
    content_content = models.TextField(default='travel_content')                    # 内容
    content_catalog = models.ForeignKey(TravelsCatalog, on_delete=models.CASCADE)


# 内容对应下的回复
class TravelCatContentComments(models.Model):
    comments_id = models.AutoField(primary_key=True, max_length=128)
    comments_user = models.ForeignKey(Persons, on_delete=models.CASCADE)  # 评论对应的人
    comments_datetime = models.DateTimeField(default='comments_time')       # 评论对应的时间
    comment_content = models.ForeignKey(TravelsCatalogContent, on_delete=models.CASCADE)   # 评论对应的回复
    comment_f_id = models.IntegerField()                                     # 对应的父评论id


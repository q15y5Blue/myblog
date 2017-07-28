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
    fans_number = models.IntegerField(default='user_fans_numbers')             # 粉丝人
    # 151310985, 158928832, 5931438
    portrait = models.CharField(default='portrait_url', max_length=1000)

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
    travel_id = models.IntegerField(default='travel_identify')            # id
    travel_title = models.CharField(max_length=1000, default='travel_title')     # 旅行标题
    travel_create_date = models.DateField(default='travel_create_date')   # 创建日期
    travel_view_number = models.IntegerField(default='travel_view_number') # 浏览人数
    travel_commended = models.BooleanField(default='travel_commend')        # 推荐欣赏与否
    travel_when = models.DateField(default='travel_date')                   # 啥时候去的
    travel_how_long = models.IntegerField(default='travel_spend_time')      # 去了多久
    travel_how_much = models.IntegerField(default='travel_cost')            # 一个人花多少钱
    travel_who = models.CharField(max_length=30, default='travel_who')      # 和谁去的
    travel_how = models.CharField(max_length=30, default='travel_how')      # 咋去的
    travel_user = models.ForeignKey(Persons, on_delete=models.CASCADE)      # 多对一 多个游记对一个人
    travel_text = models.TextField(default='travel_content_text')       # 内容 特别大


# 这个先不做
# Travel对应下的回复
class TravelComments(models.Model):
    comments_id = models.AutoField(primary_key=True, max_length=128)
    comments_user = models.ForeignKey(Persons, on_delete=models.CASCADE)  # 评论对应的人
    comments_datetime = models.DateTimeField(default='comments_time')       # 评论对应的时间
    comment_f_id = models.IntegerField(default='comment_f_id')                            # 对应的父评论id
    comment_travel = models.ForeignKey(Travels, on_delete=models.CASCADE)


# 游记下的标题分类
class TravelsCatalog(models.Model):
    catalog_title = models.CharField(max_length=32, default='travel_catalog_title')
    catalog_travel = models.ForeignKey(Travels, on_delete=models.CASCADE)
    catalog_identify = models.IntegerField(default='travel_catalog_id')

# 游记下的标题分类下的内容
class TravelsCatalogContent(models.Model):
    content_type = models.CharField(max_length=64, default='travel_cat_type')
    content_title = models.CharField(max_length=128, default='travel_cat_content')  # 文本标题 或 景点标题
    content_content = models.TextField(default='travel_content')                    # 内容
    content_catalog = models.ForeignKey(TravelsCatalog, on_delete=models.CASCADE)

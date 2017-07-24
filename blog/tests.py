from django.test import TestCase
from blog.models import Persons


#     identify = models.CharField(max_length=32,default='user_identify_id')
#     name = models.CharField(max_length=32,default='user_name')
#     describe = models.CharField(max_length=1000,default='user_describe')
#     followings = models.TextField()
#     fans = models.TextField()
class PersonTest(TestCase):
    def setUp(self):
        Persons.objects.create(identify='test', name='testname', describe='describe', followings='followings', fans='151310985,158928832,5931438')

    def test(self):
        per = Persons.objects.get(name="testname")
        list=per.getFansToList()
        print(list)
        for ls in list:
            print(ls)
        print(per.identify)
        print(per.name)
        print(per.describe)
        print(per.followings)
        print(per.fans)

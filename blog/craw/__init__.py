# 这里的作用是外部调用Django模块，使Craw模块不通过app
import sys,os
import django
pro_dir = os.getcwd()  # 如果放在project目录，就不需要在配置绝对路径了
sys.path.append(pro_dir)
os.environ['DJANGO_SETTINGS_MODULE'] ='myblog.settings'  #项目的settings
django.setup()

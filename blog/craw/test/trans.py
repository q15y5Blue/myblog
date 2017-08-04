# coding:utf8
import re

file = open('123.sql', 'r', encoding='UTF-8')
# table_name_list = re.findall('create table .*\n', str_s)
file_lines = file.readlines()
file_line_list = []# 存字符串的list
table_list = []
for line in file_lines:
    if line is not None or line.__contains__(' ') is False:
        file_line_list.append(line)
table_number = 1
for str in file_line_list:
    if str.__contains__('create table'):
        # print('开始找到第', table_number, '个表')
        table_number +=1
        star_num = file_line_list.index(str)
        table_name = re.search(r'(?<=create table).*', str).group(0)
        # update end_number\
        for end_num in range(star_num, len(file_line_list)):
            if file_line_list[end_num] == ')\n':
                break
        file_line_list[star_num+1] = table_name
        table_list.append(file_line_list[star_num+1:end_num])
        str_p = ''.join(file_line_list[star_num+1:end_num])

        # print(str_p)
        # print(star_um, " ", end_num)

for li in table_list:
    lengs = len(li)
    table_names = li[0]
    for index_t in range(1, lengs):
        param = re.search('(\s\s)\w*', li[index_t]).group(0)
        final_str = table_names.strip()+'.'+param.strip()
        # file_line_list.
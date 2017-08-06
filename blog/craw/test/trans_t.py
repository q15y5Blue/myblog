# encoding:utf8
import re

file = open('xt.txt', 'r', encoding='utf-8')
fil_source = open('123.sql', 'r', encoding='utf-8')

file_list = []
for line in file.readlines():
    file_list.append(line)
# print(file_list)
file.close()


table_list = []

index_list = []
for file_index in range(0, len(file_list)-1):
    if file_list[file_index].__contains__('NBSJ_GX.'):
        dex = file_list.index(file_list[file_index])
        index_list.append(dex)
# get table_list
for x in range(0, len(index_list)-1):
    table =[]
    table = file_list[index_list[x]:index_list[x+1]]
    table_list.append(table)
    if x == len(index_list)-2:
        table_list.append(file_list[index_list[x+1]:])
file2 = open('123.sql', 'r', encoding='utf-8')
strs=file2.read()
for table in table_list:
    # 每个table 是一个list
    for table_index in range(0, len(table)):
        if table_index == 0:
            regx = '(?<=%s\n  is \').*(?=\')' % table[table_index].strip()
            test = re.search(regx, strs)
            if test is not None:
                # print(table[table_index], end='')
                print(test.group(0))
        table_name = table[0].strip()

        # print("table_name:", table_name)
        if table_index > 0:
            column_str = re.search('\w+', table[table_index].strip())
            if column_str is not None:
                column_name = table_name+'.'+column_str.group(0).strip()
                # print("属性之名：：：", column_name)
            regx = '(?<=%s\n  is \').*(?=\')' % column_name
            reg_result = re.search(regx, strs)
            if reg_result is not None:
                print(reg_result.group(0), end='')
            else:
                print('')

        print(table[table_index], end='')
import os
import time

# print(os.sep) 输出 ‘\’

# 1.需要备份的文件与目录将被指定在一个列表中
# 必须在字符串中使用双引号，用以括起其中包含空格的名称

source=['"E:\\4.Demo\\1.python\\pythonpractice"']

# 2.备份文件必须存储在一个主备份目录中

target_dir="G:\\Data"

# 3.备份文件将打包压缩成zip文件
# 4.zip压缩文件的文件名由当前日期与时间构成

targe=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'

#如果目标目录不存在，则进行创建

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5.使用zip命令将文件打包成zip格式

zip_command='zip -r {0} {1}'.format(targe,' '.join(source))

#运行备份

print('Zip command is:')
print(zip_command)
print('Running:')

if os.system(zip_command)==0:#excute the command in a subshell
    print('Successful backup to',targe)
else:
    print('Backup FAILED')
# 当我们阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时，
# 我们需要将我们的Unicode字符串转换至一个能够被发送和接收的格式，
# 这个格式叫作“UTF-8”。我们可以在这一格式下进行读取与写入，
# 只需使用一个简单的关键字参数到我们的标准函数中：


# encoding=utf-8

import io

f=io.open("abc.txt","wt",encoding="utf-8")
f.write(u"Imagine non-English language here,我是汤姆森·克鲁斯")
f.close()

text=io.open("abc.txt",encoding="utf-8").read()
print(text)

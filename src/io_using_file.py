poem=''' \
programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

#使用内置的函数并指定文件名以及我们所希望使用的打开模式来打开一个open文件。
# 打开模式可以是阅读模式（'r'），写入模式（'w'）和追加模式（'a'）。
# 我们还可以选择是通过文本模式（'t'）还是二进制模式（'b'）来读取、写入或追加文本


# 打开文件以编辑（‘w’riting）

f=open('poem.txt','w')
# 向文件写入文本
f.write(poem)

# 关闭文件
f.close()

# 如果没有特别指定，将假定启用默认的阅读('r'ead) 模式
while True:
    line=f.readline()
    #零长度指示EOF

    if len(line)==0:
        break
    # 每行的末尾都已经有了换行符
    # 因为它是从一个文件中进行读取的
    print(line,end=' ')
#关闭文件
f.close()

# 查看帮助文档
help(open)
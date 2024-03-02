# 懒得研究了就照着网上例子写了个直接读取全部内容的低效工具——害，能用就行呗
import os

# 在脚本目录下创建的输出目录名称
path_out = "out"
str_target = "Created by KiCad"
str_replacement = "G04 EasyEDA v6.4.20.2, 2021-06-29T18:54:55+08:00*\n"

def replaceMessage(filename):
    # 按行读取文件全部内容
    lines = open(filename).readlines()

    # 读取的内容中，将含有目标字符串的一行替换为指定的内容
    for i in range(len(lines)):
        if(lines[i].find(str_target) != -1):
            print("Target string is on line %d: %s" % (i, lines[i]))
            lines[i] = str_replacement

    # 打印替换后的内容
    # for line in lines:
    #     print(line)

    # 在指定的输出路径下以相同文件名创建新文件
    file_new = open(path_out + '/' + p, 'w')

    # 将替换后的内容写入新文件
    for line in lines:
                file_new.write(line)

path = os.listdir(os.getcwd())

folder = os.path.exists(path_out)
if not folder:
    os.makedirs(path_out)
    print("Folder %s created!" % path_out)
else:
    print("Folder \"%s\" already exists!" % path_out)

num = 0
for p in path:
    if(os.path.isfile(p)):
        if(p.endswith('.gbr')):
            print("Gerber file %s" % p)
            replaceMessage(p)
            num += 1

# 统计信息输出
print("out folder: %s" % path_out)
print("Target string: \"%s\"" % str_target)
print("New string: \"%s\"" %str_replacement)
print("%d files created!" % num) 
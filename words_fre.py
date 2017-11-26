# -*- coding: utf-8 -*-
import re
import collections
import os
import os.path

# def find_file(args,dirname,files):
#     for file in files:
#         file_path = os.path.join(dirname, file)
#         if os.path.isfile(file_path):
#             print("find file:%s" % file_path)
# os.path.walk(r"USERPROFILE\desktop\log",find_file,())
filepath = 'C:\\Users\lenovo\Desktop\Log\\'

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    # for allDir in pathDir:
    #     child = os.path.join('%s%s'% (filepath, allDir))
    #     #print(child.encode('utf-8'))
    #
    #     #print(allDir)
    #     #pattern = re.compile('查询关键字*')
    #     while len(pathDir) > 0:
    #a = 0
    #a = []

    for file in pathDir:
                #child = os.path.join('%s%s' % (filepath, file))
                #filename = os.path.splitext(child)[1] == '.log'
                #filename = os.path.splitext(child)[0]
                #print(filename)
                with open(file) as f:
                    words_box=[]
                    for line in f:
                        if re.search('[签]{1}[出]{1}[8]{1}[6]{1}[9]{1}[4]{1}',line):
                           #print(pattern.findall(line))
                           #print(line)
                           #print(line.strip())
                           words_box.extend(line.strip().split('MessageContent='))
                           #count = collections.Counter(words_box)
                           #print(count)
                           #print('共签出：', len(count))
                           #for i in count:
                                # print(i)
                count = collections.Counter(words_box)
                #print(count)
                data = open("data.txt", "a")
                for i in count:
                    print(i,file=data)
                #data.close()
                #a = a + len(count)
                print(file, '：共签出：', len(count))
                print(file,'：共签出：', len(count),file=data)
                data.close()
                #a.append(len(count))
                #print(a)

        # print(words_box)
        #    return collections.Counter(words_box)
        #    count = collections.Counter(words_box)
        #    print(count)
        #return child.encode('utf-8')
# envVar = os.environ.get( "USERPROFILE" )
# print(envVar)
#print(eachFile('C:\\Users\lenovo\Desktop\Log\\'))
#for file in eachFile('C:\\Users\lenovo\Desktop\Log\\'):
#    print(file)
if __name__ == '__main__':
    eachFile(filepath)
#pattern = re.compile('keywords*')

# for file in eachFile(filepath):
#         print(file)
# file = 'C:\\Users\\lenovo\\Desktop\\Log\\2017-11-11.log'
#     def get_words(file):
#         with open (file) as f:
#             words_box=[]
#             for line in f:
#                 if re.search('查询关键字',line):
#                     #print(pattern.findall(line))
#                     #print(line)
#                     #print(line.strip())
#                     words_box.extend(line.strip().split('some words'))
                    #print(words_box)
     #    return collections.Counter(words_box)
     #    count = collections.Counter(words_box)
     #    print(count)
     #
     #    for i in count:
     #         print(i)
     #    print('共签出：',len(count))
     #
     # if __name__ == '__main__':
     #     get_words(file)

os.system("pause")

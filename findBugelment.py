#coding=utf-8
from pathlib import Path
import re

class deBugElement():
    def __init__(self):
        print('检索中...\n')

    def getFiledir(self,path):
        oat_path = []
        for child in path.iterdir():
            oat_path.append(str(child) +r'\OAT')

        return oat_path

    def getFilelist(self,path):
        filelist = path.glob('*.txt')

        return filelist

    def getFileinfo(self,filepath):
        filedict = {}
        with open(filepath,'r') as f:
            data = []
            for line in f.readlines():                
                item = line.split(' ')
                if int(item[1]) < 0 or int(item[2]) < 0 or int(item[3]) < 0 or int(item[4]) < 0:
                    data.append(item)
        return data

    def removeBug(self,path,_list):
        print('文件路径：'+ path +'\n\n文件内容为：')
        temp = ''
        with open(path,'r') as f:
            temp = f.readlines()

        for line in temp: print(line)
        print('错误数据为：')
        for item in _list: print((' ').join(item))
        y = input('是否删除(y/N)：')
        if y =='y':
            for item in _list:
                temp.remove((' ').join(item))
            print('文件已修改！！！\n文件内容为：')
            with open(path,'w+') as file:
                for line in temp:
                    file.write(line)
                    print(line)
        else : print('文件未处理！！！')

if __name__ == '__main__':
    path = Path(r'C:\Users\commo\Desktop\test')
    _deBugElement = deBugElement()
    _filedirs = _deBugElement.getFiledir(path)
    _filedict = {}
    i = 0
    for filedir in _filedirs:
        _filelist = _deBugElement.getFilelist(Path(filedir))
        for filepath in _filelist: 
            _fileitem = {}
            data = _deBugElement.getFileinfo(filepath)
            if data:
                i = 1
                print(filepath)
                _fileitem['path'] = str(filepath)
                _fileitem['_data'] = data
                _filedict[str(filepath)] = _fileitem
    for bug_path in _filedict:
        print('\n第{}条：'.format(i))
        _deBugElement.removeBug(bug_path,_filedict[bug_path]['_data'])
        i += 1

    if i == 0:
        print('没有错误数据！！！')
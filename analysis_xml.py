#coding=utf-8
import xml.etree.ElementTree as ET
from pathlib import Path

class rename():
    def __init__(self): #程序初始化
        print('begin rename ...')

    def toChangeName(self,purepath,root): #重命名文件名，并输出
        for MOAKey in root: #进入第二层树形结构
            for Text in MOAKey: #进入第三层树形结构
                ID = Text[4].text   #获取MOAKey内的Id
                FileName = Text[1].text     #获取MOAKey内的FileName
                Text_name =Text[0][1].text  #获取MOAKey内的Lable的Text内容

                new_name = ID +'.'+ Text_name +'_'+ FileName +'.avi'    #构造新的文件名，包括（id,Text,Filename),例如:1.投掷_31da28510e9e4e0496e44a0f328669aa.avi

                p = Path(purepath + FileName +'.avi')  #当前目录中的avi视频文件名
                p.rename(Path(purepath + new_name))    #将Filename的文件重命名
                print(new_name)     #输出新文件名

    def getXMLFile(self,filepath):  #获取Lables.OAT文件的XML结构
        tree = ET.parse(filepath +'Lables.OAT') #读取XML文件，根据XML文件内容结构构造树形结构
        root = tree.getroot() #获取XML文件树形结构的根结点

        return root

    def getPath(self,path): #获取已标注文件夹列表
        dirnames = []   #定义文件夹列表
        for child in path.iterdir():    #遍历文件列表
            # print(child)
            if(child.is_dir()):     #判断该文件是否是文件夹
                dirnames.append(str(child)) #将文件夹名添加文件夹列表中

        return dirnames
        
if __name__ == '__main__':
    _path = Path(r'C:\Users\commo\Desktop\新建文件夹\已标注') #全部已标注文件夹路径

    _rename = rename()  #实例化rename类

    _dirnames = _rename.getPath(_path)  #已标注文件夹列表
    for item_dirname in _dirnames:  #遍历文件夹列表
        print('\n'+ str(item_dirname))
        _root = _rename.getXMLFile(item_dirname +'\\') #获取Lables.OAT文件XML结构
        _rename.toChangeName(item_dirname +'\\',_root) #重命名已标注AVI视频文件名
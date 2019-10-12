# coding=utf-8
from board.base import conf_reader
conf_dict = conf_reader('./data/conf.ini','num')
class BaseMan():
    def __init__(self,pos,color,name):
        self.pos = pos
        self.__alive = True
        self.__name = name
        if color in ('b','r'):
            self.__color = color
        else:
            raise('color except')
    def get_name(self,):
        return self.__name
    def get_color(self,):
        return self.__color
    def kill(self):
        self.__alive = False
    def is_alive(self,):
        return self.__alive 
    def isLegal(self,pos):
        if (pos[0]>conf_dict['max_x']) or (pos[0]<conf_dict['min_x']):
            return False
        elif (pos[1]>conf_dict['max_y']) or (pos[1]<conf_dict['min_y']):
            return False
        else:
            return True
    def nextsteps(self):
        nextList = []
        x = self.pos[0] + 1
        y = self.pos[1]
        if self.isLegal([x,y]):
            nextList.append([x,y])
        x = self.pos[0]
        y = self.pos[1] + 1
        if self.isLegal([x,y]):
            nextList.append([x,y])
        x = self.pos[0] - 1
        y = self.pos[1]
        if self.isLegal([x,y]):
            nextList.append([x,y])
        x = self.pos[0]
        y = self.pos[1] - 1
        if self.isLegal([x,y]):
            nextList.append([x,y])
        return nextList

class BossMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'boss')
    def isLegal(self,pos):
        min_x = 3
        max_x = 5
        if self.get_color() == 'r':
            min_y = 0
            max_y = 2
        if self.get_color() == 'b':
            min_y = 7
            max_y = 9
 
        if (pos[0]>max_x) or (pos[0]<min_x):
            return False
        elif (pos[1]>max_y) or (pos[1]<min_y):
            return False
        else:
            return True
 
class CarMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'car')
 
if __name__ == '__main__':
    import sys
    sys.path.append('../')
    bm = BaseMan()
    print(bm.nextsteps())

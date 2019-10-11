# coding=utf-8
from board.base import conf_reader
conf_dict = conf_reader('./data/conf.ini','num')
class BaseMan():
    def __init__(self,pos,color):
        self.pos = pos
        self.alive = True
        if color in ('b','r'):
            self.color = color
        else:
            raise('color except')
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
    def kill(self):
        self.alive = False
 
class BossMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color)
        self.name = 'boss'
    def isLegal(self,pos):
        min_x = 3
        max_x = 5
        if self.color == 'r':
            min_y = 0
            max_y = 2
        if self.color == 'b':
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
        BaseMan.__init__(self,pos,color)
        self.name = 'car'
 
if __name__ == '__main__':
    import sys
    sys.path.append('../')
    bm = BaseMan()
    print(bm.nextsteps())

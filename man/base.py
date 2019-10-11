# coding=utf-8
from board.base import conf_reader
conf_dict = conf_reader('./data/conf.ini','num')
class BaseMan():
    def __init__(self,pos=[1,0]):
        self.pos = pos
        self.alive = True
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
if __name__ == '__main__':
    import sys
    sys.path.append('../')
    bm = BaseMan()
    print(bm.nextsteps())

# coding=utf-8
from board.fun import conf_reader
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
    def isOut(self,pos):
        min_x = conf_dict['min_x']
        max_x = conf_dict['max_x']
        tmp = int(conf_dict['max_y']/2)
        if self.get_color() == 'r':
            min_y = conf_dict['min_y']
            max_y = tmp
        if self.get_color() == 'b':
            min_y = tmp+1
            max_y = conf_dict['max_y']

        if (pos[0]>max_x) or (pos[0]<min_x):
            return True
        elif (pos[1]>max_y) or (pos[1]<min_y):
            return True
        else:
            return False

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
class HorseMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'horse')
    def nextsteps(self):
        nextList = []
        tmp_list = [(1,2),(2,1),(1,-2),(-2,1),
                    (-1,2),(2,-1),(-1,-2),(-2,-1)]
        for key in tmp_list:
            x = self.pos[0] + key[0]
            y = self.pos[1] + key[1]
            if self.isLegal([x,y]):
                nextList.append([x,y])
        return nextList
class MinisMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'minister')
    def nextsteps(self):
        nextList = []
        tmp_list = [(2,2),(2,-2),(-2,2),(-2,-2)]
        for key in tmp_list:
            x = self.pos[0] + key[0]
            y = self.pos[1] + key[1]
            if self.isLegal([x,y]):
                if not self.isOut([x,y]):
                    nextList.append([x,y])
        return nextList
class GuardMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'guard')
    def nextsteps(self):
        nextList = []
        tmp_list = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for key in tmp_list:
            x = self.pos[0] + key[0]
            y = self.pos[1] + key[1]
            if self.isLegal([x,y]):
                nextList.append([x,y])
        return nextList
class SoldierMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'soldier')
    def nextsteps(self):
        nextList = []
        x = self.pos[0]
        tmp_dict = {'r':1,'b':-1}
        y = self.pos[1] + tmp_dict[self.get_color()]
        if self.isLegal([x,y]):
            nextList.append([x,y])
        if self.isOut(self.pos):
            tmp_list = [(1,0),(-1,0)]
            for key in tmp_list:
                x = self.pos[0] + key[0]
                y = self.pos[1] + key[1]
                if self.isLegal([x,y]):
                    nextList.append([x,y])
        return nextList
if __name__ == '__main__':
    import sys
    sys.path.append('../')
    bm = BaseMan()
    print(bm.nextsteps())

# coding=utf-8
from Chess.board.fun import conf_reader
class BaseMan():
    def __init__(self,pos,color,name):
        self.pos = (int(pos[0]),int(pos[1]))
        self.__alive = True
        self.__name = name
        self.conf_dict = conf_reader('./data/conf.ini','num')
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
    def isLegal(self,pos,input_df):
        if (pos[0]>self.conf_dict['max_x']) or (pos[0]<self.conf_dict['min_x']):
            return False
        elif (pos[1]>self.conf_dict['max_y']) or (pos[1]<self.conf_dict['min_y']):
            return False
        elif (self.get_color() == input_df[str(pos[0])][int(pos[1])][1]):
            return False
        else:
            return True
    def isOut(self,pos):
        min_x = self.conf_dict['min_x']
        max_x = self.conf_dict['max_x']
        tmp = int(self.conf_dict['max_y']/2)
        if self.get_color() == 'r':
            min_y = self.conf_dict['min_y']
            max_y = tmp
        if self.get_color() == 'b':
            min_y = tmp+1
            max_y = self.conf_dict['max_y']

        if (pos[0]>max_x) or (pos[0]<min_x):
            return True
        elif (pos[1]>max_y) or (pos[1]<min_y):
            return True
        else:
            return False

    def nextsteps(self,input_df):
        nextList = []
        x = self.pos[0] + 1
        y = self.pos[1]
        if self.isLegal([x,y],input_df):
            nextList.append((x,y))
        x = self.pos[0]
        y = self.pos[1] + 1
        if self.isLegal([x,y],input_df):
            nextList.append((x,y))
        x = self.pos[0] - 1
        y = self.pos[1]
        if self.isLegal([x,y],input_df):
            nextList.append((x,y))
        x = self.pos[0]
        y = self.pos[1] - 1
        if self.isLegal([x,y],input_df):
            nextList.append((x,y))
        return nextList
    def get_col_index(self,input_df):
        df = input_df.copy()
        tmp = df[df.index!=int(self.pos[1])]
        list_colum = list(tmp[str(self.pos[0])])
        tmp = df.drop(str(self.pos[0]),axis=1)
        list_index = list(tmp.loc[int(self.pos[1])])
        return list_index,list_colum

class BossMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'boss')
    def isLegal(self,pos,input_df):
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
        elif (self.get_color() == input_df[str(pos[0])][int(pos[1])][1]):
            return False
        else:
            return True
    def pos_utl_man(self,input_list,n):
        res = {'flag':False,'pos':(0,0)}
        for index,key in enumerate(input_list):
            if 'no' == key[0]:
                continue
            elif 'boss' == key[0]:
                res['flag'] = True
                res['pos'] = (self.pos[0],self.pos[1]+(index+1)*n)
                break
            else:
                break
        return res
    def nextsteps(self,input_df):
        nextList = BaseMan.nextsteps(self,input_df)
        if self.get_color() == 'r':
            n = 1
            input_list = list(input_df[str(self.pos[0])][int(self.pos[1])+1:input_df.shape[0]])
        elif self.get_color() == 'b':
            n = -1
            input_list = list(input_df[str(self.pos[0])][0:int(self.pos[1])])
            input_list.reverse()
        res = self.pos_utl_man(input_list,n)
        if res['flag'] == True:
            nextList.append(res['pos'])
        return nextList

class CarMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'car')
    def pos_utl_man(self,num,input_list,input_df,axis=0):
        res_list = []
        if (0 == axis):
            for key in input_list:
                if ('no' != input_df[str(key)][num][0]):
                    if (self.get_color() != input_df[str(key)][num][1]):
                        res_list.append((key,num))
                    break
                else:
                    res_list.append((key,num))
        elif (1 == axis):
            for key in input_list:
                if ('no' != input_df[str(num)][key][0]):
                    if (self.get_color() != input_df[str(num)][key][1]):
                        res_list.append((num,key))
                    break
                else:
                    res_list.append((num,key))
        else:
            raise KeyError(axis)
        return res_list
    def nextsteps(self,input_df):
        nextList = []
        #list_index,list_colum = self.get_col_index(input_df)
        df = input_df.copy()
        input_list = list(range(0,self.pos[0]))
        input_list.reverse()
        list_pos = self.pos_utl_man(int(self.pos[1]),input_list,df,axis=0)
        nextList.extend(list_pos)

        input_list = list(range(self.pos[0]+1,self.conf_dict['max_x']+1))
        list_pos = self.pos_utl_man(int(self.pos[1]),input_list,df,axis=0)
        nextList.extend(list_pos)

        input_list = list(range(0,self.pos[1]))
        input_list.reverse()
        list_pos = self.pos_utl_man(int(self.pos[0]),input_list,df,axis=1)
        nextList.extend(list_pos)

        input_list = list(range(self.pos[1]+1,self.conf_dict['max_y']+1))
        list_pos = self.pos_utl_man(int(self.pos[0]),input_list,df,axis=1)
        nextList.extend(list_pos)

        return nextList
class HorseMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'horse')
    def nextsteps(self,input_df):
        nextList = []
        tmp_list = [(1,2),(-1,2),(1,-2),(-1,-2),
                    (2,1),(2,-1),(-2,1),(-2,-1)]
        hinders = [(0,1),(0,-1),(1,0),(-1,0)]
        for num in range(len(hinders)):
            x_h = self.pos[0] + hinders[num][0]
            y_h = self.pos[1] + hinders[num][1]
            if (x_h<int(self.conf_dict['min_x']) or x_h>int(self.conf_dict['max_x']) or
                y_h<int(self.conf_dict['min_y']) or y_h>int(self.conf_dict['max_y'])):
                continue
            elif ('no' == input_df[str(x_h)][y_h][0]):
                x = self.pos[0] + tmp_list[num*2][0]
                y = self.pos[1] + tmp_list[num*2][1]
                if self.isLegal([x,y],input_df):
                    nextList.append((x,y))
                x = self.pos[0] + tmp_list[num*2+1][0]
                y = self.pos[1] + tmp_list[num*2+1][1]
                if self.isLegal([x,y],input_df):
                    nextList.append((x,y))
        return nextList
class MinisMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'minister')
    def nextsteps(self,input_df):
        nextList = []
        tmp_list = [(2,2),(2,-2),(-2,2),(-2,-2)]
        hinders = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for num in range(len(hinders)):
            x_h = self.pos[0] + hinders[num][0]
            y_h = self.pos[1] + hinders[num][1]
            if (x_h<int(self.conf_dict['min_x']) or x_h>int(self.conf_dict['max_x']) or
                y_h<int(self.conf_dict['min_y']) or y_h>int(self.conf_dict['max_y'])):
                continue
            elif ('no' == input_df[str(x_h)][y_h][0]):
                x = self.pos[0] + tmp_list[num][0]
                y = self.pos[1] + tmp_list[num][1]
                if self.isLegal([x,y],input_df):
                    if not self.isOut([x,y]):
                        nextList.append((x,y))
        return nextList
class GuardMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'guard')
    def isLegal(self,pos,input_df):
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
        elif (self.get_color() == input_df[str(pos[0])][int(pos[1])][1]):
            return False
        else:
            return True
    def nextsteps(self,input_df):
        nextList = []
        tmp_list = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for key in tmp_list:
            x = self.pos[0] + key[0]
            y = self.pos[1] + key[1]
            if self.isLegal([x,y],input_df):
                nextList.append((x,y))
        return nextList
class SoldierMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'soldier')
    def nextsteps(self,input_df):
        nextList = []
        x = self.pos[0]
        tmp_dict = {'r':1,'b':-1}
        y = self.pos[1] + tmp_dict[self.get_color()]
        if self.isLegal([x,y],input_df):
            nextList.append((x,y))
        if self.isOut(self.pos):
            tmp_list = [(1,0),(-1,0)]
            for key in tmp_list:
                x = self.pos[0] + key[0]
                y = self.pos[1] + key[1]
                if self.isLegal([x,y],input_df):
                    nextList.append((x,y))
        return nextList
class CannonMan(BaseMan):
    def __init__(self,pos,color):
        BaseMan.__init__(self,pos,color,'cannon')
    def pos_utl_man(self,num,input_list,input_df,axis=0):
        res_list = []
        flag = True
        if (0 == axis):
            for key in input_list:
                if flag:
                    if ('no' != input_df[str(key)][num][0]):
                        flag = False
                    else:
                        res_list.append((key,num))
                else:
                    if ('no' != input_df[str(key)][num][0]):
                        if (self.get_color() != input_df[str(key)][num][1]):
                            res_list.append((key,num))
                            break
        elif (1 == axis):
            for key in input_list:
                if flag:
                    if ('no' != input_df[str(num)][key][0]):
                        flag = False
                    else:
                        res_list.append((num,key))
                else:
                    if ('no' != input_df[str(num)][key][0]):
                        if (self.get_color() != input_df[str(num)][key][1]):
                            res_list.append((num,key))
                            break
        else:
            raise KeyError(axis)
        return res_list
    def nextsteps(self,input_df):
        nextList = []
        #list_index,list_colum = self.get_col_index(input_df)
        df = input_df.copy()
        input_list = list(range(0,self.pos[0]))
        input_list.reverse()
        list_pos = self.pos_utl_man(int(self.pos[1]),input_list,df,axis=0)
        nextList.extend(list_pos)

        input_list = list(range(self.pos[0]+1,self.conf_dict['max_x']+1))
        list_pos = self.pos_utl_man(int(self.pos[1]),input_list,df,axis=0)
        nextList.extend(list_pos)

        input_list = list(range(0,self.pos[1]))
        input_list.reverse()
        list_pos = self.pos_utl_man(int(self.pos[0]),input_list,df,axis=1)
        nextList.extend(list_pos)

        input_list = list(range(self.pos[1]+1,self.conf_dict['max_y']+1))
        list_pos = self.pos_utl_man(int(self.pos[0]),input_list,df,axis=1)
        nextList.extend(list_pos)

        return nextList

if __name__ == '__main__':
    import sys
    sys.path.append('../')
    bm = BaseMan()
    print(bm.nextsteps())

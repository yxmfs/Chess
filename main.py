#!/usr/bin/env python3
import pandas as pd
from man import base
from board.base import BaseBoard
from board.fun import switch,read_sql_df,save_sql_df
from man.base import *

class Game():
    def __init__(self,):
        self.board = BaseBoard()
        self.board.init_status()
        b_man = self.init_all_man('b')
        r_man = self.init_all_man('r')
        self.all_man = {'b':b_man,'r':r_man}
    def test_print(self,bm):
        print('the status is:\n',self.board.get_status())
        print('its pos :{0},its name :{1}, its color:{2}'.format(bm.pos,bm.get_name(),bm.get_color()))
        print('now it is pos is :{0}'.format(bm.pos))
        print('the next pos may be :{0}'.format(bm.nextsteps()))
    def init_all_man(self,color):
        l = [key for key in range(5)] 
        all_man = {'guard':l.copy(), 'cannon':l.copy(), 'soldier':l.copy(), 'car':l.copy(),
                'minister':l.copy(), 'boss':l.copy(), 'horse':l.copy()}
        all_list = ['guard','cannon','soldier','car','minister','boss','horse']
        for key in all_man.keys():
            tmp = self.board.get_all_pos(key,color)
            m = self.select_one_man(key)
            for ele in tmp:
                all_man[key][ele[2]] = m(ele[0],ele[1])
        return all_man
    def select_one_man(self,name):
        for case in switch(name):
            if case('boss'):
                return BossMan
                break
            if case('car'):
                return CarMan
                break
            if case('horse'):
                return HorseMan
                break
            if case('minister'):
                return MinisMan
                break
            if case('soldier'):
                return SoldierMan
                break
            if case('guard'):
                return GuardMan
                break
            if case('cannon'):
                return CannonMan
                break
            if case(): # default, could also just omit condition or 'if True'
                s = 'Unknow name:' + name
                raise KeyError(s)
    def get_select_man(self,data):
        return self.all_man[data[1]][data[0]][data[2]]
    def flash_pos(self,select_man_pos):
        print('now flash the pos')
        data = self.board.find_data(select_man_pos[0],select_man_pos[1])
        the_man = self.get_select_man(data)
        self.test_print(the_man)
def main():
    game = Game()
    game.flash_pos([1,2])
if __name__ == '__main__':
    main()

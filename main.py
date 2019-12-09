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
        self.all_name = ['guard','cannon','soldier','car','minister','boss','horse']
    def test_print(self,bm):
        print('the status is:\n',self.board.get_status())
        print('its pos :{0},its name :{1}, its color:{2}'.format(bm.pos,bm.get_name(),bm.get_color()))
        print('now it is pos is :{0}'.format(bm.pos))
        print('the next pos may be :{0}'.format(bm.nextsteps(self.board.get_status())))
    def get_log(self,log):
        print(log)
    def init_all_man(self,color):
        l = [key for key in range(5)] 
        all_man = {'guard':l.copy(), 'cannon':l.copy(), 'soldier':l.copy(), 'car':l.copy(),
                'minister':l.copy(), 'boss':l.copy(), 'horse':l.copy()}
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
    def isMan(self,data):
        #board data order:name ,color, number
        if data[0] in self.all_name:
            return True
        else:
            return False
    def isOver(self):
        if not self.all_man['r']['boss'][0].is_alive():
            self.get_log('the black man has win!')
            return True
        elif not self.all_man['b']['boss'][0].is_alive():
            self.get_log('the red man has win!')
            return True
        else:
            return False
    def get_man_by_data(self,data):
        try:
            return self.all_man[data[1]][data[0]][data[2]]  #find man class by color, name, number
        except Exception as e:
            self.get_log('the data given has no man!')
            raise KeyError(e)
    def get_man_by_pos(self,select_pos):
        select_data = self.board.find_data(select_pos[0],select_pos[1])
        if self.isMan(select_data):
            select_man = self.get_man_by_data(select_data)
            self.test_print(select_man)
            return select_data,select_man
        else:
            self.get_log('the select place has no man!')
            return None,None
    def update_pos(self,select_data,select_man,target_pos):
        if select_data == None:
            self.get_log('can not get select data')
            return None
        self.get_log('now update the pos')
        if target_pos in select_man.nextsteps(self.board.get_status()):
            target_data = self.board.find_data(target_pos[0],target_pos[1])
            if self.isMan(target_data):  #target place has a man
                if target_data[1] != select_data[1]:  #select and target man has different color
                    target_man = self.get_select_man(target_data)
                    target_man.kill()
                else:
                    self.get_log('it is a ilegal target place!')
            self.board.replace_data(target_pos[0],target_pos[1],select_data)
            self.board.replace_data(select_man.pos[0],select_man.pos[1],('no','no','no'))
            select_man.pos = (int(target_pos[0]),int(target_pos[1]))
        else:
            self.get_log('it is a ilegal target place!')

def main():
    game = Game()
    while (not game.isOver()):
        x = input("输入x值")
        y = input("输入y值")
        target_x = input("输入目标x值")
        target_y = input("输入目标y值")
        select_data,select_man = game.get_man_by_pos([int(x),int(y)])
        game.update_pos(select_data,select_man,[int(target_x),int(target_y)])

if __name__ == '__main__':
    main()

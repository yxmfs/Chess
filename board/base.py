import pandas as pd
from board.fun import conf_reader

class BaseBoard():
    def __init__(self,):
        self.__conf_dict = conf_reader('./data/conf.ini','num')
        t_s = 'no'
        temp_list = [(t_s,t_s,t_s) for _ in range(self.__conf_dict['max_y']+1)]
        temp_dict = {}
        for key in range(self.__conf_dict['max_x']+1):
            temp_dict[str(key)] = temp_list
        self.__status = pd.DataFrame(temp_dict)
        self.__sort_dict = {0:'boss',1:'car',2:'horse'}
    def get_status(self,):
        #print(self.__status.shape)
        return self.__status.copy()
    def find_data(self,x,y):
        return self.__status[str(x)][y]
    def replace_data(self,x,y,data):
        self.__status[str(x)][y] = data
    def init_status(self,):
        self.replace_data('0',0, ('car','r',0))
        self.replace_data('8',0, ('car','r',1))
        self.replace_data('1',0, ('horse','r',0))
        self.replace_data('7',0, ('horse','r',1))
        self.replace_data('2',0, ('minister','r',0))
        self.replace_data('6',0, ('minister','r',1))
        self.replace_data('3',0, ('guard','r',0))
        self.replace_data('5',0, ('guard','r',1))
        self.replace_data('4',0, ('boss','r',0))
        self.replace_data('1',2, ('cannon','r',0))
        self.replace_data('7',2, ('cannon','r',1))
        self.replace_data('0',3, ('soldier','r',0))
        self.replace_data('2',3, ('soldier','r',1))
        self.replace_data('4',3, ('soldier','r',2))
        self.replace_data('6',3, ('soldier','r',3))
        self.replace_data('8',3, ('soldier','r',4))

        self.replace_data('0',9, ('car','b',0))
        self.replace_data('8',9, ('car','b',1))
        self.replace_data('1',9, ('horse','b',0))
        self.replace_data('7',9, ('horse','b',1))
        self.replace_data('2',9, ('minister','b',0))
        self.replace_data('6',9, ('minister','b',1))
        self.replace_data('3',9, ('guard','b',0))
        self.replace_data('5',9, ('guard','b',1))
        self.replace_data('4',9, ('boss','b',0))
        self.replace_data('1',7, ('cannon','b',0))
        self.replace_data('7',7, ('cannon','b',1))
        self.replace_data('0',6, ('soldier','b',0))
        self.replace_data('2',6, ('soldier','b',1))
        self.replace_data('4',6, ('soldier','b',2))
        self.replace_data('6',6, ('soldier','b',3))
        self.replace_data('8',6, ('soldier','b',4))
    def get_all_pos(self,name,color):
        result = []
        df = self.get_status()
        for x in df.columns:
            for y in range(len(df[x])):
                if df[x][y][0] == name:
                    if df[x][y][1] == color:
                        result.append([(x,y),df[x][y][1],df[x][y][2]])  #list[pos,color,num]
        return result
    def get_all_name(self,num):
        result = []
        df = self.get_status()
        f = lambda x: x[num]
        for key in df.columns:
            result.extend(list(df[key].apply(f)))
        return set(result)
if __name__ == '__main__':
    print(conf_reader('./data/conf.ini','num'))
    bb = BaseBoard()
    bb.init_status()
    print(bb.get_status())

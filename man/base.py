from board.base import read_conf_dict
conf_dict = read_conf_dict('./data/conf.ini','num')
class BaseMan():
    def __init__(self,pos=[1,0]):
        self.pos = pos
    def isLegal(pos):
        if (pos[0]<=conf_dict['max_x']) and (pos[0]>=conf_dict['min_x']):
            return True
    def nextstep(self):
        nextList = []
    
        

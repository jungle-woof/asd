# coding=utf-8


class Config:
    """配置参数"""
    def __init__(self,numofexp=10,myrange=10,hasfraction=False,hasmulanddiv=False,maxnumofoper=3,hasparentheses=False,hasneg=False):
        self.numofexp = numofexp
        self.myrange  = myrange
        self.hasfraction = hasfraction
        self.__hasmulanddiv = hasmulanddiv
        self.hasparentheses = hasparentheses
        self.hasneg = hasneg
        self.maxnumofoper = maxnumofoper
        self.__answer = True

    @staticmethod
    def create(self,args):
        if args is None:
            return  Config()
        # for i in len(args):
        #     tem_config = config(args[i],)

    def isHasMultipleAndDivide(self):
        return self.__hasmulanddiv

    def __str__(self):
        if not self.hasneg:
            negmsg = '否'
        else:
            negmsg = '是'
        return "是否有负数:{}".format(negmsg)
    def get_answer(self):
        return  self.__answer

if __name__ == '__main__':
    tempconfig = Config(hasneg=True)
    print(tempconfig)



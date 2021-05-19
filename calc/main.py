# coding=utf-8
import string
from model.config import Config
from  generator import Generator
if __name__ == '__main__':
    mygen = Generator()
    print("设置题目难度\n")
    numofexp = int(raw_input("请输入题目数量:\t"))
    myrange = int(raw_input("请输入数字范围:\t"))
    hasfraction = raw_input("式子中是否有分数(Y or N):\t").upper()
    hasmulanddiv = raw_input("式子中是否包含乘除法(Y or N):\t").upper()
    hasparentheses = raw_input("式子中是否带有括号(Y or N):\t").upper()
    hasneg = raw_input("式子中是否有负数(Y or N):\t").upper()
    maxnumofoper = int(raw_input("请输入运算符数量:(目前最多支持3种)\t"))
    if maxnumofoper >3:
        print("请重新输入运算符数量")
        maxnumofoper = raw_input("请输入运算符数量:(目前最多支持3种)\t")
    if hasfraction.upper() == "Y":
        hasfraction = True
    elif hasfraction == "N":
        hasfraction = False
    else:
        print("请重新输入式子中是否有分数(Y or N):\t")
    if hasmulanddiv == "Y":
        hasmulanddiv = True
    elif hasmulanddiv == "N":
        hasmulanddiv = False
    else:
        print("请重新输入式子中是否包含乘除法(Y or N):\t")
    if hasparentheses == "Y":
        hasparentheses = True
    elif hasparentheses == "N":
        hasparentheses = False
    else:
        print("请重新输入式子中是否带有括号(Y or N):\t")
    if hasneg == "Y":
        hasneg = True
    elif hasneg == "N":
        hasneg = False
    else:
        print("请重新输入式子中是否有负数(Y or N):\t")
    myconf = Config(hasfraction=hasfraction, hasneg=hasneg, hasmulanddiv=hasmulanddiv, hasparentheses=hasparentheses, numofexp=numofexp, myrange=myrange)
    set_expression = mygen.generate(myconf)
    ret = mygen.format_expression(set_expression)
    print("您此次作答作对{}题,答错了{}题".format(ret["right"],ret["wrong"]))
    # print(ret)
    

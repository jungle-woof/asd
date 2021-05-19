# coding=utf-8
import random
from model.constants import Constants
from model.expression import Expression
from binary_tree import Tree
from answer import Answer
class Generator:
    """表达式生成类"""
    def __init__(self):
        pass

    def format_expression(self,set_express):
        print("***** start format expression *****")
        set_re = []
        right = 0
        wrong = 0
        if not set_express:
            return "空空如也"
        else:
            for i, exp in enumerate(set_express):
                str1 = str(i) + ": " + exp.tostring()+"\n"
                str2 = exp.tostring()
                set_re.append(str2)

                with open('expression.txt', 'a+') as f:
                    f.write(str1)
                ans = raw_input("第" + str(i+1) + "题: " + exp.get_expression() + "\n")
                if ans == str(exp.get_value()):
                    right = right + 1
                else:
                    wrong = wrong + 1


                # print(str1)
            return {
                "right": right,
                "wrong": wrong
            }

    def generate(self, config):

        print("***** start generate expression *****")
        numofexp = config.numofexp
        set = []
        # randomNumberOfOperation 操作符随机数目

        for i in range(numofexp):
            random_number_of_operation = random.randint(1, config.maxnumofoper + 1)
            mark_fraction =0
            if config.hasfraction:
                mark_fraction = random.randint(0,random_number_of_operation+1)*2

            # 操作数的数目 = 操作符的数目 + 1
            numberOfOpand = random_number_of_operation + 1
            exp = []
            for j in range(random_number_of_operation+numberOfOpand):
                if j % 2 == 0:
                    if j == mark_fraction and config.hasfraction:
                        exp.append(self.generator_oprand(True,config.myrange))
                    else:
                        exp.append(self.generator_oprand(self.random_flag(config.hasfraction),config.myrange))
                    if j > 1 and exp[j-1] == Constants.DIVIDE and str(exp[j]) == Constants.ZERO:
                        # could not be ÷ 0 ,  generator operator from + - x
                        exp[j - 1] = self.pick_an_operation(self.generate_available_operators(
                        config.isHasMultipleAndDivide()))

                else:
                    exp.append(self.pick_an_operation(self.generate_available_operators(
                        config.isHasMultipleAndDivide())))

            expression = ""

            if config.hasparentheses and numberOfOpand != 2:
                expression = " ".join(self.mark_parentheses(exp,numberOfOpand))
            else:
                expression = " ".join(exp)

            if self.has_duplicate(set, expression):
                print("有重复的啦啦啦啦啦")
                i = i - 1
                continue
            else:
                expre = Expression(expression)
                set.append(expre)

        if config.get_answer():
            wnum = Answer.answer_one(set)
            if wnum > 0:
                print("-----------" + str(wnum) + "-----------")
                config.numofexp = wnum
                set1 = self.generate(config)
                set.extend(set1)
        return set

    # 判重逻辑
    def has_duplicate(self, set_express, expression):
        for item in set_express:
            if self.is_duplicate(item.get_expression(), expression):
                return True
        return False

    # 判重
    def is_duplicate(self, expression1, expression2):
        if Tree.generate_expression(Tree.create(expression1).get_root()) == Tree.\
                generate_expression(Tree.create(expression2).get_root()):
            return True
        else:
            return False


    # 生成括号表达式
    def mark_parentheses(self, exp, numberOfOpand):

        expression = []
        num = numberOfOpand
        if exp:
            length = len(exp)
            left_position = random.randint(0, (num/2))
            right_position = random.randint(left_position+1, (num/2)+1)
            mark = -1
            for i in range(length):
                if self.is_operation(exp[i]):

                    expression.append(exp[i])
                else:
                    mark = mark + 1
                    if mark == left_position:
                        expression.append(Constants.LEFT_PARENTHESES)
                        expression.append(exp[i])
                    elif mark == right_position:
                        expression.append(exp[i])
                        expression.append(Constants.RIGHT_PARENTHESES)
                    else:
                        expression.append(exp[i])
        if expression[0] == "(" and expression[-1] == ")":
            expressions = self.mark_parentheses(exp,numberOfOpand)
            return expressions
        return expression

    # 判断是否为运算符
    def is_operation(self, item):
        return {
            '+': True,
            '-': True,
            'x': True,
            '÷': True
        }.get(item, False)

    # 是否生成分数随机判断
    def random_flag(self, flag):
        return bool(random.getrandbits(1)) if flag else False

    # 生成操作数
    def generator_oprand(self, is_fraction, _range):
        return self.generate_an_fraction(_range) if is_fraction else str(random.randint(0, _range))

    # 生成分数
    def generate_an_fraction(self, _range):
        denominator = random.randint(2, _range+1)
        numerator = random.randint(1, denominator)
        while denominator == numerator:
            denominator = random.randint(2, _range + 1)
            numerator = random.randint(1, denominator)
        left_Integer = random.randint(0, 1)
        # 是否生成带分数的随机标识
        max_multiple = self.gcd(denominator, numerator)
        denominator = denominator / max_multiple
        numerator = numerator / max_multiple
        fraction = ""
        if left_Integer == 0:
            fraction = str(numerator) + Constants.VIRGULE + str(denominator)
        else:
            fraction = str(left_Integer) + Constants.SINGLE_QUOTE + str(numerator) + Constants.VIRGULE + str(denominator)
        return fraction

    # 求得分子分母最大公约数
    def gcd(self, demo, nume):
        if nume == 0:
            return demo
        r = demo % nume
        return self.gcd(nume, r)

    # 随机取得一个+ - * ÷运算符
    def pick_an_operation(self, operators, *args):
        if args:
            operators.append(args)
        return operators[random.randint(0,len(operators))-1]

    # 得到配置参数要求的运算符集合
    @staticmethod
    def generate_available_operators(hasMultipleAndDivide):
        if hasMultipleAndDivide:
            return [Constants.PLUS, Constants.MINUS, Constants.MULTIPLY, Constants.DIVIDE]
        return [Constants.PLUS, Constants.MINUS]


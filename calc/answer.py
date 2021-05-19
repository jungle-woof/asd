# coding=utf-8
from fractions import Fraction

from binary_tree import Tree
from model.constants import Constants
from model.expression import Expression
from model.stack import Stack


class Answer:
    def __init__(self):
        self.wronum = 0
    @staticmethod
    def answer_one(set_expression):
        wnum = 0
        if set_expression:
            for exp in set_expression:
                flag = Answer.answer_two(exp)
                if flag == 1:
                    set_expression.remove(exp)
                    wnum = wnum +1
        return wnum
    @staticmethod
    def answer_two(expression):
        an = Answer()
        stack = Stack()
        result = Fraction(0, 1)
        # testsuff = "1 1 chu 0 chu 1'1/5 chu 2 +".split(" ")
        suffix = Tree.infix_to_suffix(expression.get_expression())
        str = " ".join(suffix)
        # print(str)
        if not suffix:
            return
        is_num = None
        for item in suffix:
            try:
                is_num = True
                result = Answer.get_fraction(item)
            except Exception:
                is_num = False
            if is_num:
                stack.push(result)
            else:
                flag = {
                    '+': 1,
                    '-': 2,
                    'x': 3,
                    '÷': 4,
                }.get(item, 5)
                if flag == 1:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(a + b)
                elif flag == 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b - a)
                elif flag == 3:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(a * b)
                elif flag == 4:
                    a = stack.pop()
                    b = stack.pop()
                    if a == 0:
                        print("you 0")
                        an.wronum = 1
                        break
                    stack.push(b / a)
                elif flag == 5:
                    pass
        expression.set_fraction(stack.peek())
        expression.set_value(stack.peek())
        return an.wronum

    @staticmethod
    def get_fraction(item):
        result = 0
        if item.find(Constants.VIRGULE) > 0:
            attach = 0
            right = ""
            if item.find(Constants.SINGLE_QUOTE) > 0:
                parts = item.split(Constants.SINGLE_QUOTE)
                attach = int(parts[0])
                right = parts[1]
            else:
                right = item

            parts = right.split(Constants.VIRGULE)
            return Fraction(attach * int(parts[1]) + int(parts[0]), int(parts[1]))
        else:
            result = int(item);
            return Fraction(result, 1)



if __name__ == '__main__':
    ans = Answer()
    exp = Expression("1 + 2 - 5")
    ans.answer_two(exp)
    print(exp.tostring())




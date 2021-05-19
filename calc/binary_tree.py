# coding:utf-8
from model.stack import Stack
from model.constants import Constants

class Node(object):
    """节点"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    """二叉树"""
    output = []

    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root
    @staticmethod
    def generate_expression(root):
        if not root.left:
            if not root.right:
                return root.value
        elif root.value == "+" or root.value == "x":
            left = Tree.generate_expression(root.left)
            right = Tree.generate_expression(root.right)
            if cmp(left, right) <=0:
                return root.value + left + right
            else:
                return root.value + right + left
        else:
            return root.value + Tree.generate_expression(root.left) + Tree.generate_expression(root.right);
        pass
    # 生成二叉树表示表达式
    @staticmethod
    def create(exp):
        Tree.output = []
        # return Tree.infix_to_suffix(exp)
        return Tree.construct(Tree.infix_to_suffix(exp))
        # st = "54 x 23 + +".split(" ")
        # return Tree.construct(st)
    # 转成后缀表达式
    @staticmethod
    def infix_to_suffix(exp):
        Tree.output = []
        theStack = Stack()
        if not exp:
            return []
        infix = exp.split(" ")
        length = len(infix)
        for j in range(length):
            item = infix[j]
            flag = {
                '+': 1,
                '-': 1,
                'x': 2,
                '÷': 2,
                '(': 3,
                ')': 4
            }.get(item, 5)
            if flag == 1:
                Tree.get_oper(item, 1, theStack)
            elif flag == 2:
                Tree.get_oper(item, 2, theStack)
            elif flag == 3:
                theStack.push(item)
            elif flag == 4:
                Tree.got_paren(theStack)
            elif flag == 5:
                Tree.output.append(item)
        while not theStack.is_empty():
            Tree.output.append(theStack.pop())
        return Tree.output

    @staticmethod
    def got_paren(stack):
        while not stack.is_empty():
            item = stack.pop()
            if item == "(":
                break
            else:
                Tree.output.append(item)

    @staticmethod
    def get_oper(opthis, prec1, stack):
        while not stack.is_empty():
            optop = stack.pop()
            if optop == "(":
                stack.push(optop)
                break
            else:
                prec2 = 0
                if optop == "+" or optop == "-":
                    prec2 = 1
                else:
                    prec2 = 2
                if prec2 < prec1:
                    stack.push(optop)
                    break
                else:
                    Tree.output.append(optop)
        stack.push(opthis)

    def add(self, item):
        """添加节点"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            # print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        # print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        # print(node.elem, end=" ")
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        # print(node.elem, end=" ")

    @staticmethod
    def construct(post):
        """构造二叉树"""
        stack = Stack()
        # parent = None
        # right = None
        # left = None
        for item in post:
            if not Tree.is_operator(item):
                parent = Node(item)
                stack.push(parent)
            else:
                parent = Node(item)
                right = stack.pop()
                left = stack.pop()
                parent.right = right
                parent.left = left
                stack.push(parent)

        parent = stack.peek()
        stack.pop()
        return Tree(parent)

    @staticmethod
    def is_operator(item):
        ops = Tree.generate_available_operators(True)
        # print(ops)
        # print(item in ops)
        if item in ops:
            return True
        else:
            return False

    @staticmethod
    def generate_available_operators(hasMultipleAndDivide):
        if hasMultipleAndDivide:
            return [Constants.PLUS, Constants.MINUS, Constants.MULTIPLY, Constants.DIVIDE]
        return [Constants.PLUS, Constants.MINUS]

if __name__ == "__main__":
    tree = Tree()
    # tree.add(0)
    # tree.add(1)
    # tree.add(2)
    # tree.add(3)
    # tree.add(4)
    # tree.add(5)
    # tree.add(6)
    # tree.add(7)
    # tree.add(8)
    # tree.add(9)
    # tree.breadth_travel()
    # print(" ")
    # tree.preorder(tree.root)
    # print(" ")
    # tree.inorder(tree.root)
    # print(" ")
    # tree.postorder(tree.root)
    # print(" ")
    print(Tree.create("( 2 + 3 ) + 5 x 4"))

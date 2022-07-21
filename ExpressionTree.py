#  File: ExpressionTree.py

#  Description: Makes an expression tree to evaluate an expression. It will also make them into postorder and preorder

#  Student's Name: Johnny Tran

#  Student's UT EID: jht825

#  Partner's Name: Crystal Le

#  Partner's UT EID: cl44964

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 4/10/22

#  Date Last Modified: 4/11/22

import sys


operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        self.root = Node()
        stack = Stack()
        current = self.root
        expr = expr.split()
        # goes through the expression
        for i in expr:
            # if it's a (
            if i == '(':
                current.lChild = Node()
                stack.push(current)
                current = current.lChild
            
            # checks if the current expression is in the operators
            elif i in operators:
                current.data = i 
                stack.push(current)
                current.rChild = Node()
                current = current.rChild
            
            # checks if the current expression is a digit
            elif '.' in i:
                current.data = float(i)
                current = stack.pop()

            elif i.isdigit():
                current.data = i
                current = stack.pop()
                
            elif len(i) > 1:
                current.data = int(i)
                current = stack.pop()
            
            # checks if the current expression is )
            elif i == ')':
                if stack.is_empty() == False:
                    current = stack.pop()
        
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        if aNode:
            left = str(self.evaluate(aNode.lChild))
            right = str(self.evaluate(aNode.rChild))
            return float(eval(left + str(aNode.data) + right) )
        else:
            return ''

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        # empty list to hold
        lst = []
        # empty string to print out
        strng = ''
        #run recursively to add into a list
        if aNode is not None:
            lst.append(str(aNode.data))
            lst.append(self.pre_order(aNode.lChild).strip())
            lst.append(self.pre_order(aNode.rChild).strip())

        # loop into a string
        for i in lst:
            strng += str(i) + ' '
        return strng

    
    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        # empty list to hold
        lst = []
        # empty string to print out
        strng = ''
        #run recursively though a helper function
        #run recursively to add into a list
        if aNode is not None:
            lst.append(self.post_order(aNode.lChild).strip())
            lst.append(self.post_order(aNode.rChild).strip())
            lst.append(str(aNode.data))
        # loop into a string
        for i in lst:
            strng += str(i) + ' '
        return strng


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, '=', str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print('Prefix Expression:', tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print('Postfix Expression:', tree.post_order(tree.root).strip())


if __name__ == '__main__':
    main()
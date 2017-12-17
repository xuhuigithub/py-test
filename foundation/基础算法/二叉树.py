#!/bin/env python
#coding:utf-8
"""
reference: https://github.com/qiwsir/algorithm/blob/master/binary_tree.md
二叉树查找的性质：
1、若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2、任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
3、任意节点的左、右子树也分别为二叉查找树。
4、没有键值相等的节点（no duplicate nodes）。

"""

class Node(object):
    """
    二叉树左右枝
    """
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self,data,parent=None):
        """
        遍历二叉树
        """
        if data < self.data:
            if self.left is None:
                return None,None
            return self.left.lookup(data,self)
        elif data > self.data:
            if self.right is None:
                return None,None
            return self.right.lookup(data,self)
        else:
            return self,parent
if __name__ == '__main__':
    root = Node(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    root.insert(4)
    root.insert(7)
    root.insert(14)
    root.insert(13)
    node,parent = root.lookup(6)
    print node,parent

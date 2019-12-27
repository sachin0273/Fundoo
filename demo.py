# import sys
#
# print(dir(tuple))
# uu = (1, 2, 3, 4, 5, "kk", [])
# print(sys.maxsize)
# print(-sys.maxsize - 1)
# ui = (0, 0, 0)
# o = uu.__repr__()
# print(o)
#
# if o == uu.__str__() and uu.__ge__(ui):
#     print('ddjdd')
# print(uu.__gt__(ui))
# # print(True)

import json
import pdb

# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert(value, self.root)
#
#     def _insert(self, value, cur_node):
#         if value < cur_node.value:
#             if cur_node.left_child is None:
#                 cur_node.left_child = Node(value)
#             else:
#                 self._insert(value, cur_node.left_child)
#         elif value > cur_node.value:
#             if cur_node.right_child is None:
#                 cur_node.right_child = Node(value)
#             else:
#                 self._insert(value, cur_node.right_child)
#         else:
#             print('value already in tree')
#
#     def print_tree(self):
#         if self.root is not None:
#             self._print_tree(self.root)
#
#     def _print_tree(self, cur_node):
#         if cur_node is not None:
#             self._print_tree(cur_node.left_child)
#             print(str(cur_node.value))
#             self._print_tree(cur_node.right_child)
#
#     def height(self):
#         if self.root is not None:
#             return self._height(self.root, 0)
#
#     def _height(self, cur_node, cur_height):
#         if cur_node is None: return cur_height
#         left_height = self._height(cur_node.left_child, cur_height + 1)
#         right_hight = self._height(cur_node.right_child, cur_height + 1)
#         return max(left_height, right_hight)
#
#     def search(self, value):
#         if self.root is not None:
#             return self._search(value, self.root)
#         else:
#             return False
#
#     def _search(self, value, cur_node):
#         if value == cur_node.value:
#             return True
#         elif value < cur_node.value and cur_node.left_child is not None:
#             return self._search(value, cur_node.left_child)
#         elif value > cur_node.value and cur_node.right_child is not None:
#             return self._search(value, cur_node.right_child)
#         return False
#
#     def minValueNode(self, node):
#         current = node
#
#         # loop down to find the leftmost leaf
#         while current.left_child is not None:
#             current = current.left_child
#         return current
#
#     def deleteNode(self, root, value):
#
#         # Base Case
#         # pdb.set_trace()
#         if root is None:
#             return root
#
#             # If the key to be deleted is smaller than the root's
#         # key then it lies in  left subtree
#         if value < root.value:
#             root.left_child = self.deleteNode(root.left_child, value)
#
#             # If the kye to be delete is greater than the root's key
#         # then it lies in right subtree
#         elif value > root.value:
#             root.right_child = self.deleteNode(root.right_child, value)
#
#             # If key is same as root's key, then this is the node
#             # to be deleted
#         else:
#
#             # Node with only one child or no child
#             if root.left_child is None:
#                 temp = root.right_child
#                 root = None
#                 return temp
#
#             elif root.right_child is None:
#                 temp = root.left_child
#                 root = None
#                 return temp
#
#                 # Node with two children: Get the inorder successor
#             # (smallest in the right subtree)
#             temp = self.minValueNode(root.right_child)
#
#             # Copy the inorder successor's content to this node
#             print(temp.value, 'jjjjjjjjjjjjjjjjjjjjjjjjjj')
#             root.value = temp.value
#
#             # Delete the inorder successor
#
#             root.right_child = self.deleteNode(root.right_child, temp.value)
#
#         return root
#
#     def printPostorder(self):
#         if self.root:
#             self._printPostorder(self.root)
#
#     def _printPostorder(self, root):
#
#         if root:
#             # First recur on left child
#             self._printPostorder(root.left_child)
#
#             # the recur on right child
#             self._printPostorder(root.right_child)
#
#             # now print the data of node
#             print(root.value)
#
#     def printPreorder(self):
#         if self.root:
#             self._printPreorder(self.root)
#
#     def _printPreorder(self, root):
#
#         if root:
#             # First print the data of node
#             print(root.value),
#
#             # Then recur on left child
#             self._printPreorder(root.left_child)
#
#             # Finally recur on right child
#             self._printPreorder(root.right_child)
#
#
# def fill_tree(tree, num_elems=100, max_int=1000):
#     from random import randint
#     for _ in range(num_elems):
#         cur_elem = randint(0, max_int)
#         tree.insert(cur_elem)
#     return tree
#
#
# tree = BinaryTree()
# # tree1 = fill_tree(tree)
#
#
# tree.insert(20)
# tree.insert(5)
# tree.insert(2)
# tree.insert(25)
# tree.insert(22)
# tree.insert(30)
# tree.print_tree()
#
# print('tree height is', tree.height())
#
# print(tree.search(5))
# print(tree.search(0))
# ui = tree.minValueNode(tree.root)
# print(ui.value)
# di = tree.deleteNode(tree.root, 5)
# print(di.value)
# print('after deletion in order \n \n')
# tree.print_tree()
# print('this is postorder \n \n')
# tree.printPostorder()
# print('using preorder \n \n')
# tree.printPreorder()


# class Node:
#     def __init__(self, data):
#         self.item = data
#         self.nref = None
#         self.pref = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.start_node = None
#
#     def insert_at_start(self, data):
#         if self.start_node is None:
#             new_node = Node(data)
#             self.start_node = new_node
#             print("node inserted")
#             return
#         new_node = Node(data)
#         new_node.nref = self.start_node
#         self.start_node.pref = new_node
#         self.start_node = new_node
#
#     def insert_at_end(self, data):
#         if self.start_node is None:
#             new_node = Node(data)
#             self.start_node = new_node
#             return
#         n = self.start_node
#         while n.nref is not None:
#             n = n.nref
#         new_node = Node(data)
#         n.nref = new_node
#         new_node.pref = n
#
#     def insert_after_item(self, x, data):
#         if self.start_node is None:
#             print("List is empty")
#             return
#         else:
#             n = self.start_node
#             while n is not None:
#                 if n.item == x:
#                     break
#                 n = n.nref
#             if n is None:
#                 print("item not in the list")
#             else:
#                 new_node = Node(data)
#                 new_node.pref = n
#                 new_node.nref = n.nref
#                 if n.nref is not None:
#                     n.nref.prev = new_node
#                 n.nref = new_node
#
#     def insert_before_item(self, x, data):
#         if self.start_node is None:
#             print("List is empty")
#             return
#         else:
#             n = self.start_node
#             while n is not None:
#                 # print(n.item)
#                 if n.item == x:
#                     break
#                 n = n.nref
#                 # print(n)
#             if n is None:
#                 print("item not in the list")
#             else:
#                 new_node = Node(data)
#                 new_node.nref = n
#                 new_node.pref = n.pref
#                 if n.pref is not None:
#                     n.pref.nref = new_node
#                 n.pref = new_node
#
#     def reverse_linked_list(self):
#         if self.start_node is None:
#             print("The list has no element to delete")
#             return
#         p = self.start_node
#         q = p.nref
#         p.nref = None
#         p.pref = q
#         while q is not None:
#             q.pref = q.nref
#             q.nref = p
#             p = q
#             q = q.pref
#         self.start_node = p
#
#     def traverse_list(self):
#         if self.start_node is None:
#             print("List has no element")
#             return
#         else:
#             n = self.start_node
#             while n is not None:
#                 print(n.item, " ")
#                 n = n.nref
#
#
# if __name__ == '__main__':
#     Dl = DoublyLinkedList()
#     Dl.insert_at_start(2)
#     Dl.insert_at_start(3)
#     Dl.insert_before_item(2, 23)
#     Dl.insert_after_item(2, 24)
#     Dl.traverse_list()
#     Dl.reverse_linked_list()
#     Dl.traverse_list()
import sys
from pprint import pprint

# printing json response
data = {'status': 'OK', 'results': [{'address_components': [{'long_name': 'Rajpath', 'types': ['route'],
                                                             'short_name': 'Rajpath'}, {'long_name': 'India Gate',
                                                                                        'types': ['political',
                                                                                                  'sublocality',
                                                                                                  'sublocality_level_1'],
                                                                                        'short_name': 'India Gate'},
                                                            {'long_name': 'New Delhi', 'types':
                                                                ['locality', 'political'], 'short_name': 'New Delhi'},
                                                            {'long_name': 'New Delhi',
                                                             'types': ['administrative_area_level_2', 'political'],
                                                             'short_name': 'New Delhi'}, {'long_name':
                                                                                              'Delhi', 'types': [
        'administrative_area_level_1', 'political'], 'short_name': 'DL'}, {'long_name':
                                                                               'India',
                                                                           'types': ['country', 'political'],
                                                                           'short_name': 'IN'},
                                                            {'long_name': '110001', 'types':
                                                                ['postal_code'], 'short_name': '110001'}],
                                     'geometry': {'location': {'lng': 77.2295097, 'lat': 28.612912},
                                                  'viewport': {
                                                      'northeast': {'lng': 77.2308586802915, 'lat': 28.6142609802915},
                                                      'southwest': {'lng':
                                                                        77.22816071970848, 'lat': 28.6115630197085}},
                                                  'location_type': 'APPROXIMATE'}, 'types':
                                         ['establishment', 'point_of_interest'],
                                     'formatted_address': 'Rajpath, India Gate, New Delhi, Delhi 110001',
                                     'place_id': 'ChIJC03rqdriDDkRXT6SJRGXFwc'}]}

print(data)

# class all:
#     def __init__(self):
#         self.jh = 00
#
#     def it(self):
#         return self.jh
#
#
# class y(all):
#     def __init__(self):
#         all.__init__(self)
#
#
# gh = y()
# print(gh.it())
# ui = 'dsdksssm'
# if isinstance(gh, all):
#     print('ya ya ')
# if isinstance(ui, all):
#     print('ddkjdd')
# if issubclass(y, all):
#     print('fdhdjusdn')
# print(y.__mro__)
# print(y.mro())
#
#
# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""
#
#     @classmethod
#     def gh(cls, iii):
#         return iii
#
#     def __init__(self, max=0):
#         self.max = max
#
#     def __iter__(self):
#         self.min = 0
#         return self
#
#     def __next__(self):
#         if self.min <= self.max:
#             result = 2 ** self.min
#             self.min += 1
#             return result
#         else:
#             raise StopIteration
#
#
# a = PowTwo(4)
# i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))
# for i in PowTwo(5):
#     print(i)
# matrix = ['f', 'ff', 'hk']
# flattened = [n for row in matrix for n in row]
# print(flattened)
# first_letters = set()
# words = 'sachin'
# for w in words:
#     print(w[0])
#     first_letters.add(w[0])
# print(first_letters)
# count = 0
# gh = {w for w in words}
# valu = [9, 9, 90, 766, 55]
# exp = ['kl', 'jk', 'jlm']
# kl = {'jkl': 8989, 'kjih': 889}
# flipped = {key: value for key, value in kl.items()}
# print(flipped)
# print(a.gh('juiyh'))

# number = '100'
# print(float(number))
# import array
#
# arr = array.array('i', [9, 8, 9])
# for i in arr:
#     print(i)
# x, y = input("Enter a two value: ").split()
# print(x)
# print(y)
# x = list(map(int, input("Enter a multiple value: ").split()))
# print("List of students: ", x)

# x, y, z = [int(x) for x in input("Enter three value: ").split()]
# print(x, y, z)

fg = {'kl': 89, 'lj': 0}
tg = fg.pop('kl')
print(fg)
print(tg)


class CustomException(BaseException):
    pass


class new(CustomException):
    pass


g = 2
try:
    if 1 == g:
        raise new('hi error is occurred')
except new as e:
    print(e)
finally:
    print('kahlil')

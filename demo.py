import sys

print(dir(tuple))
uu = (1, 2, 3, 4, 5, "kk", [])
print(sys.maxsize)
print(-sys.maxsize - 1)
ui = (0, 0, 0)
o = uu.__repr__()
print(o)

if o == uu.__str__() and uu.__ge__(ui):
    print('ddjdd')
print(uu.__gt__(ui))
# print(True)

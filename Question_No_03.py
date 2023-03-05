#from binarytree import build,Node

#creating list for tree

list1=[42,68,39,9,53,76,5,10,61,71,87,17,56,79]


#It is constructing wrong binary tree


#now

#root=Node(42)
#root.left=Node(39)
#root.left.left=Node(9)
#root.left.left.left=Node(5)
#root.left.left.right=Node(10)
#root.left.left.right.right=Node(17)
#root.right=Node(68)
#root.right.right=Node(76)
#root.right.right.left=Node(71)
#root.right.right.right=Node(87)
#root.right.right.right.left=Node(79)
#root.right.left=Node(53)
#root.right.left.right=Node(61)
#root.right.left.right.left=Node(56)

#print(root)

from anytree import Node,RenderTree
from anytree.exporter import DotExporter

num1=Node(42)
num2=Node(39,parent=num1)
num3=Node(9,parent=num2)
num4=Node(5,parent=num3)
num5=Node(10,parent=num2)
num6=Node(17,parent=num5)
num13=Node(68,parent=num1)
num7=Node(76,parent=num13)
num8=Node(71,parent=num7)
num9=Node(87,parent=num7)
num10=Node(79,parent=num9)
num11=Node(53,parent=num13)
num12=Node(61,parent=num11)
num14=Node(56,parent=num12)

for pre, fill, node in RenderTree(num1):
    print("%s%s" % (pre, node.name))

from anytree.exporter import DotExporter
DotExporter(num1).to_picture("udo.png")


import re


class variable :
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.frequency = 0

def increase_fre(self):
    self.frequency = self.frequency+1

class node:
    def __init__(self,name,key):
        self.name = name
        self.key = key
        self.right = None
        self.left = None

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.key< node.key:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
    return root

def rightRotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    return y

def  leftRotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

def splay(root,key):
    if root == None or root.key== key :
        return root
    if root.key> key:
        if root.left == None:
            return root
        if (root.left.key> key):
            root.left.left = splay(root.left.left,key)
            root = rightRotate(root)
        elif root.left.key< key :
            root.left.right = splay(root.left.right,key)
            if root.left.right != None:
                root.left = leftRotate(root.left)
        if root.left == None:
            return root
        else:
            return rightRotate(root)
    else:
        if root.right == None:
            return root
        if root.right.key> key:
            root.right.left = splay(root.right.left, key)
            if root.right.left != None :
                root.right = rightRotate(root.right)
        elif root.right.key< key :
            root.right.right = splay(root.right.right,key)
            root = leftRotate(root)
        if root.right == None :
            return root
        else:
            return leftRotate(root)

def search(root,key):
    if root == None :
        return False
    elif root.key== key:
        return True
    elif root.key>key:
        return search(root.left, key)
    elif root.key<key:
        return search(root.right, key)


def matcher(listvar,txt,root):
    pattern_1 = "^int"
    pattern_print = "^printf"
    if re.match(pattern_1,txt) :
        array = txt.split('=')
        array2 = array[0].split()
        array3 = array[1].split(';')
        array3[0]=array3[0].lstrip()
        var = variable(array2[1],int(array3[0]))
        listvar.append(var)
        return listvar,root

    elif re.match(pattern_print,txt) :
        array = txt.split(',')
        l = array[len(array)-1]
        names = []
        for i in range(len(array)-1):
            if i>=1:
                names.append(array[i])
        var = l[0]
        names.append(var)
        print(names)
        for i in names:
            flag=0
            iz = 0
            needed = None
            while iz<len(listvar) and flag!=1 :
                try:
                    if listvar[iz].name == i:
                        needed = listvar[iz]
                        flag+=1
                except :
                    print()
                iz+=1
            if flag==0:
                print("variable undeclared")
            else :
                if search(root,needed.value):
                    root = splay(root,needed.value)
                    print("now the root is ",root.name,"and value is",root.key)
                else:
                    root = insert(root,node(needed.name,needed.value))
                    root = splay(root,needed.value)
                    print("now the root is ", root.name, "and value is", root.key)
        return listvar,root

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.name,"  ",root.key)
        inorder(root.right)

#def printer(root,canvas):

'''listval = []
root = None
txt1 = "int x = 10;"
listval,root = matcher(listval,txt1,root)
print(listval)
txt2 = "int y = 5;"
listval,root = matcher(listval,txt2,root)
print(listval)
txt3 = "int z = 20;"
listval,root = matcher(listval,txt3,root)
print(listval)

txt4 = 'printf("%d",x);'
listval,root = matcher(listval,txt4,root)
inorder(root)
print(root.name)

txt5 = 'printf("%d",y);'
listval,root = matcher(listval,txt5,root)
inorder(root)
print(root.name)

txt6 = 'printf("%d",z);'
listval,root = matcher(listval,txt6,root)
inorder(root)
print(root.name)

txt7 = 'printf("%d",x);'
listval,root = matcher(listval,txt7,root)
inorder(root)
print(root.name)
'''

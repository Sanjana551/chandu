#implement binary search trce and its operations using list 
 
class Node:
 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.key)
        inorder(root.right)
def preorder(root):
    if root is not None:
        print(root.key)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key)
 
 
 
def insert(node, key):
 
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    return node
 
 
 
def minValueNode(node):
    current = node
 
    while(current.left is not None):
        current = current.left
 
    return current
 
 
 
def deleteNode(root, key):
 
    if root is None:
        return root
 
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    else:
 
        
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 

        temp = minValueNode(root.right)
 
        
        root.key = temp.key
 
        
        root.right = deleteNode(root.right, temp.key)
 
    return root
 
 

if __name__ == '__main__':
    global start
    root = None    
    
     
    x = int(input("no of operations"))
    for i in range (x):
        n = int(input("code"))
    
    
        if n == 1:
            print('insert  the value into tree')
            n2=int(input("value insert"))  
            root = insert(root, n2)
        if n == 2:
            print(" inoder traversal of the BST")
            inorder(root)
        if n == 3:
            print("preoder traversal of the BST")
            preorder(root)

        if n == 4:
            print("postorder traversal of the BST")
            postorder(root)
        if n == 5:
            print('delete the element from  the tree')
            n2=int(input("value delete"))   
            root = deleteNode(root, n2)
        if n == 6:
            break
 



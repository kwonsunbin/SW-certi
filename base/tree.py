class node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    global preorder_to_print
    if not root :
        return
    preorder_to_print.append(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    global inorder_to_print
    if not root :
        return
    inorder(root.left)
    inorder_to_print.append(root.data)
    inorder(root.right)

def postorder(root):
    global postorder_to_print
    if not root :
        return
    postorder(root.left)
    postorder(root.right)
    postorder_to_print.append(root.data)
    

if __name__ == "__main__":
    n1 = node('A')
    n2 = node('B')
    n3 = node('C')
    n4 = node('D')
    n5 = node('E')
    n6 = node('F')
    n7 = node('G')
    n8 = node('H')
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    root = n1

    preorder_to_print = [] 
    preorder(root)
    print(preorder_to_print)

    inorder_to_print = [] 
    inorder(root)
    print(inorder_to_print)

    postorder_to_print = [] 
    postorder(root)
    print(postorder_to_print)

    